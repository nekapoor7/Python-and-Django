try:
    import os
    import sys
    import datetime
    import time
    import boto3
    print("All Modules Loaded ...... ")
except Exception as e:
    print("Error {}".format(e))


class MyDb(object):

    def __init__(self, Table_Name ='DHT'):
        self.Table_Name=Table_Name
        self.db = boto3.resource('dynamodb')
        self.table = self.db.Table(Table_Name)

        self.client = boto3.client('dynamodb')

    @property
    def get(self):
        response = self.table.get_item(
            Key={
                'Sensor_id':"1"
            }
        )

        return response

    def put(self, Sensor_id='' , Humidity='',Temperature=''):
        self.table.put_item(
            Item={
                'Sensor_id':Sensor_id,
                'Humidity' :Humidity,
                'Temperature': Temperature
            }
        )

    def delete(self,Sensor_id=''):
        self.table.delete_item(
            Key={
                'Sensor_Id': Sensor_id
            }
        )

    def describe_table(self):
        response = self.client.describe_table(
            TableName='DHT'
        )
        return response

obj = MyDb()
print(obj.describe_table())

resp = obj.put(Sensor_id='2',Humidity='99' ,Temperature='99')
print(resp)

