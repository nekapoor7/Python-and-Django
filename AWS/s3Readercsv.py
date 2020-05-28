try:
    import boto3
    import pandas as pd
    import os
    import sys
    print("All Modules are Loaded")
except Exception as e:
    print("Some Modules are missing{}".format(e))

class S3Reader:
    def __init__(self,Bucket_Name='',Key=''):
        self.Bucket_Name = Bucket_Name
        self.Key = Key
        self.client = boto3.client('s3')

    @property
    def get_def(self):
        response = self.client.list_objects(Bucket=self.Bucket_Name)
        


