import boto3
import logging
import boto3
from botocore.exceptions import ClientError

session = boto3.session.Session(profile_name='DeepRacer')
s3_1=session.client('s3')
s3 = session.resource('s3')
response = s3_1.list_buckets()

for bucket in response['Buckets']:
    t=bucket["Name"]
    bucket=s3.Bucket(t)
    total_size=0
    for file in bucket.objects.all():
        total_size += file.size

    if total_size==0:
        print('Bucket Vide: Name of Bucket -->',bucket.name,'Size-->',total_size)
        #bucket.objects.all().delete()
        bucket.delete()
        
    else:
        print('Bucket pleine: Name of Buckcet -->',bucket.name,'Size-->',total_size)