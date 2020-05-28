import os
import sys
import boto3
import pandas as pd
import matplotlib.pyplot as plt
import datetime


d = datetime.datetime.now()
Current_time = "{}{}{}".format(d.month,d.day,d.year)

client = boto3.client('s3')
with open("C:\\Users\\nekapoor\\git\\GreecePic.jpg","rb") as f:
    data = f.read()

response = client.put_object(
    ACL='private',
    Body=data,
    Bucket='nehakapoor{}'.format(Current_time),
    Key='GreecePic.jpg',
)

with open("C:\\Users\\nekapoor\\git\\apple.jpg","rb") as f:
    data = f.read()

response = client.put_object(
    ACL='private',
    Body=data,
    Bucket='nehakapoor{}'.format(Current_time),
    Key='apple.jpg',
)
