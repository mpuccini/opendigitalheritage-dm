import os

class Config(object):
    # mongodb
    mongo_db = os.getenv('MONGO_DATABASE')
    mongo_uri = os.getenv('MONGO_URI')
    # data lake
    store_type = os.getenv('STORE_TYPE')
    aws_s3_bucket = os.getenv('AWS_S3_BUCKET')
    aws_s3_region = os.getenv('AWS_S3_REGION')
    fs_host = os.getenv('FS_HOST')
    fs_path= os.getenv('FS_PATH')

    SECRET_KEY = os.urandom(32)
