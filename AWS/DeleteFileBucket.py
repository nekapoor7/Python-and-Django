import os
import sys
import boto3
import pandas as pd
import matplotlib.pyplot as plt
import datetime


d = datetime.datetime.now()
Current_time = "{}{}{}".format(d.month,d.day,d.year)
client = boto3.client('s3')
response = client.delete_object(
    Bucket='nehakapoor{}'.format(Current_time),
    Key='GreecePic.jpg'
)
print(response)