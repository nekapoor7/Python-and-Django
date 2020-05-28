import os
import sys
import boto3
import pandas as pd
import matplotlib.pyplot as plt
import datetime


d = datetime.datetime.now()
Current_time = "{}{}{}".format(d.month,d.day,d.year)

client = boto3.client('s3')
response = client.create_bucket(
    ACL='private',
    Bucket='nehakapoor{}'.format(Current_time),
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    }
)
print(response)

with open("C:\\Users\\nekapoor\\git\\greece.jpg","rb") as f:
    data = f.read()

response = client.put_object(
    ACL='private',
    Body=data,
    Bucket='nehakapoor{}'.format(Current_time),
    Key='greece.jpg',
)

response = client.delete_object(
    Bucket='nehakapoor{}'.format(Current_time),
    Key='GreecePic.jpg'
)
print(response)

