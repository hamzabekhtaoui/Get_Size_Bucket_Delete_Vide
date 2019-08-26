import boto3
import logging
import boto3
from botocore.exceptions import ClientError

session = boto3.session.Session(profile_name='DeepRacer')
s3_1=session.client('s3')
s3 = session.resource('s3')
response = s3_1.list_buckets()
for bucket in response['Buckets']:
    t=bucket['Name']
    bucket_versioning= s3.BucketVersioning(t)
    #Enable_Versioning
    bucket_versioning.enable()
    #Disable_Versioning
    #bucket_versioning.suspend()
