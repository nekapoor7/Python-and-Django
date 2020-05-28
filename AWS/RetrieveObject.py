import os
import sys
import boto3
import pandas as pd
import matplotlib.pyplot as plt
import datetime


d = datetime.datetime.now()
Current_time = "{}{}{}".format(d.month,d.day,d.year)
client = boto3.client('s3')


response = client.list_objects_v2(
    Bucket='nehakapoor{}'.format(Current_time)
)
for x in response.get("Contents",None):
    print(x.get("Key",None))

response = client.list_buckets()
print(response)

for x in response.get("Buckets",None):
    print(x.get("Name",None))