import os
import boto3

s3_client = boto3.resource('s3')

# s3_client = boto3.client('s3', aws_access_key_id=os.environ["S3_AWS_ACCESS_KEY_ID"], aws_secret_access_key=os.environ["S3_AWS_SECRET_ACCESS_KEY"])

#s3_client.put_object(Body="HelloWorld!", Bucket='myhstore', Key='test')



bucket = s3_client.Bucket('myhstore').objects.all()

for obj in bucket:
    print(obj)


#    arn:aws:s3:::myhstore
