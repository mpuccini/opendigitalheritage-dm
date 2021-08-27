import os, shutil
import hashlib
import configparser
import argparse
import logging
#import boto3
from pymongo import MongoClient
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

DEFAULT_CONFIGFILE = 'config.ini'
BUF_SIZE = 409600




def loadConf():     
    '''     
    Load cofiguration from ini file passed as argument     

    Returns     
    -------     
    config : obj     
    '''     
       
    config = configparser.ConfigParser()     
             
    config.read('config.ini')     
          

    return config


c=loadConf()
print(c['mongo']['db'])
