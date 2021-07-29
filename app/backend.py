import os, shutil
import hashlib
import configparser
import argparse
import logging
import boto3
from pymongo import MongoClient
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

DEFAULT_CONFIGFILE = 'config.ini'
BUF_SIZE = 409600


parser = argparse.ArgumentParser(description='PoC ENEA Heritage Science Internship 2021 - Upload/Research data module')
parser.add_argument('-l',                     
		    '--log',                     
		    dest='logLevel',                     
		    choices=['DEBUG','INFO','ERROR'],                     
		    help='Log level',                     
		    default='ERROR')
parser.add_argument('-cf',                     
		    '--configFile',                     
		    help='Configuration file path',                     
		    default=DEFAULT_CONFIGFILE)

args, unknown = parser.parse_known_args()

## Logging
level = logging.getLevelName(args.logLevel)
logging.basicConfig(format='%(levelname)s: %(message)s', level=level)
log = logging.getLogger(__name__)


def loadConf():     
    '''     
    Load cofiguration from ini file passed as argument     

    Returns     
    -------     
    config : obj     
    '''     
    log.debug("Loading configuration from %s", args.configFile)     
    config = configparser.ConfigParser()     
    try:         
        config.read(args.configFile)     
    except Exception as e:         
        log.error("Cannot read configuration file %s: %s", args.configFile, e)         
        raise Exception("Cannot read configuration file")     
    log.debug("Configuration: %s", config)         

    return config


def connect2mongo(conf,collection):
    '''
    Establishes connection with mongoDB

    Parameters
    ----------
    collection : str
        collection name where to store data on mongoDB

    Returns 
    -------
    collection : str
        returns a connection to defined collection
    '''
    c = conf['mongo']
    if not c:
        log.error("Cannot get configuration!")
        raise Exception("Cannot get configuration")

    try:
        client = MongoClient(c['uri'])
        coll = client[c['db']][collection]
    except Exception:
        log.error("Cannot connect to mongo (check if you're under ENEA VPN)")
        raise Exception("Cannot connect to mongo")
    
    log.info("Connection to mongo succeded!")

    return coll


def upload2mongo(doc, collection):
    '''
    Upload document to mongoDB collection

    Returns 
    -------
    none
    '''
    # Don't known if "doc" is printable (check __repr__ magic method)
    log.debug("Uploading %s to MongoDB", doc)
    try:        
        c = loadConf()
    except Exception as e:
        log.error("Cannot read configuration")
        return
    
    try:
        log.debug("Connecting to mongo with conf %s", c)
        coll = connect2mongo(c, collection)
    except Exception as e:
        # Better catch more significative exception types
        # (if connect2mongo() raises some)
        log.error("Cannot connect to mongo: %s", e)
        return

    log.debug("Inserting new document")    
    indoc = coll.insert_one(doc)    

    # Add reference into inventory
    inventory = connect2mongo(c, 'inventory')
    invdoc = {}
    invdoc['title'] = doc['title']
    invdoc['project'] = doc['project']
    invdoc['objtype'] = doc['objtype']
    invdoc['year'] = doc['year']
    invdoc['coordinates'] = {}
    invdoc['coordinates']['latitude'] = doc['coordinates']['latitude']
    invdoc['coordinates']['longitude'] = doc['coordinates']['longitude']
    invdoc['ID'] = indoc.inserted_id
    inventory.insert_one(invdoc)
    '''    if coll.count_documents({'document_hash': doc['document_hash']}) > 0:
        # Insert try/except here?
        log.debug("Updating document %s", doc['document_hash'])
        coll.update_one(
            {'document_hash': doc['document_hash']}, 
            {'$push': {'found_for_hashtags': doc['found_for_hashtags'][0]}},
            upsert=True)
    else:
        log.debug("Inserting new document")
        # Insert try/except here?
        coll.insert_one(doc)
    log.debug("Uploaded data to mongo")'''

def connect2S3():
    try:
        s3_client = boto3.client('s3')
    except Exception:
        log.error("Cannot connect to Amazon S3")
        raise Exception("Cannot connect Amazon S3")
    
    log.info("Connection to Amazon S3 succeded!")

    return s3_client


def upload2S3(obj, bucket_name, obj_key):
    """
    Upload a file from a local folder to an Amazon S3 bucket, using the default
    configuration.
    """
    s3 = connect2S3()
    s3.upload_file(
        obj,
        bucket_name,
        obj_key)


def makeHash(path):
    '''
    Get a file and calculates hash

    Paramenters
    -----------
    path : str
        file path

    Returns
    -------
    hash : str
        hash of the file
    '''

    # Maybe add option to process in chunks
    log.debug("Computing MD5 hash for %s", path)
    md5 = hashlib.md5()
    try:
        with open(path, 'rb') as f:
            data = f.read(BUF_SIZE)
            md5.update(data)
    except IOError as ioe:
        log.error("Cannot open/read file %s: %s", path, ioe)
        raise
    except Exception as e:
        log.error("Generic error while reading file %s: %s", path, e)
        raise

    digest = md5.hexdigest()
    log.debug("MD5 digest is %s", digest)
    
    return digest


def workOnObj(obj, store_type):
    c = loadConf()
    savepathroot = c['datastore']['path']
    tmpsavepath = savepathroot+secure_filename(obj.filename)
    obj.save(tmpsavepath)
    objhash = makeHash(tmpsavepath)
    split_obj = os.path.splitext(obj.filename)
    extension = split_obj[1]
    hashname = objhash+extension
    if store_type == 'fs':
        newsavepath = savepathroot
        if not os.path.exists(newsavepath):             
            os.makedirs(newsavepath)
            shutil.move(tmpsavepath,newsavepath+'/'+hashname)
    elif store_type == 's3':
        upload2S3(tmpsavepath, 'myhstore', hashname)
    return objhash, extension
