import os, shutil
import hashlib
#import configparser
import argparse
import logging
import boto3
from pymongo import MongoClient
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from config import Config
import io

BUF_SIZE = 409600

parser = argparse.ArgumentParser(description='ENEA Open Digital Twins - Upload/Search data module')
parser.add_argument('-l',                     
		    '--log',                     
		    dest='logLevel',                     
		    choices=['DEBUG','INFO','ERROR'],                     
		    help='Log level',                     
		    default='ERROR')

args, unknown = parser.parse_known_args()

## Logging
level = logging.getLevelName(args.logLevel)
logging.basicConfig(format='%(levelname)s: %(message)s', level=level)
log = logging.getLogger(__name__)


def connect2mongo(uri, db, collection):
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

    try:
        client = MongoClient(uri)
        coll = client[db][collection]
    except Exception:
        log.error("Cannot connect to mongo (check if you're under ENEA VPN)")
        raise Exception("Cannot connect to mongo")
    
    log.info("Connection to mongo succeded!")

    return coll


def upload2mongo(doc, uri, db, collection):
    '''
    Upload document to mongoDB collection

    Returns 
    -------
    none
    '''
    # Don't known if "doc" is printable (check __repr__ magic method)
    log.debug("Uploading %s to MongoDB", doc)
    
    try:
        log.debug("Connecting to mongo db.collection: %s.%s", db, collection)
        coll = connect2mongo(uri, db, collection)
    except Exception as e:
        # Better catch more significative exception types
        # (if connect2mongo() raises some)
        log.error("Cannot connect to mongo: %s", e)
        return

    log.debug("Inserting new document")    
    indoc = coll.insert_one(doc)    

    # Add reference into inventory
    inventory = connect2mongo(uri, db, 'inventory')
    invdoc = {}
    invdoc['title'] = doc['metadata']['asset']['title']
    invdoc['coordinates'] = {}
    invdoc['coordinates']['latitude'] = doc['metadata']['asset']['coordinates']['latitude']
    invdoc['coordinates']['longitude'] = doc['metadata']['asset']['coordinates']['longitude']
    invdoc['project_name'] = doc['metadata']['project']['name']
    invdoc['project_year'] = doc['metadata']['project']['year']
    invdoc['project_url'] = doc['metadata']['project']['url']

    invdoc['objtype'] = doc['objectdata']['type']

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
    s3_client = connect2S3()
    s3_client.put_object(
        Body=obj, 
        Bucket=bucket_name, 
        Key=obj_key)    


def makeHash(obj):
    '''
    Get a file and calculates hash

    Paramenters
    -----------
    obj : bytes
        file bytes to hash

    Returns
    -------
    hash : str
        hash of the file
    '''

    # Maybe add option to process in chunks
    log.debug("Computing MD5 hash for %s", obj.filename)
    md5 = hashlib.md5()
    
    try:
        data = obj.read(BUF_SIZE)
        md5.update(data)
    except IOError as ioe:
        log.error("Cannot open/read file %s: %s", obj.filename, ioe)
        raise
    except Exception as e:
        log.error("Generic error while reading file %s: %s", obj.filename, e)
        raise

    digest = md5.hexdigest()
    log.debug("MD5 digest is %s", digest)
    
    return digest



def workOnObj(obj, store_type):
#    filename = secure_filename(obj.filename)
    objhash = makeHash(obj)
    filename_base, extension = os.path.splitext(obj.filename)

    hashname = objhash+extension
    if store_type == 'fs':
        obj.stream.seek(0)
        obj.save(os.path.join(os.getenv('FS_PATH'),hashname))
    elif store_type == 's3':
        c = Config()
        obj.stream.seek(0)
        upload2S3(obj.stream, c.aws_s3_bucket, hashname)
    return objhash, extension




