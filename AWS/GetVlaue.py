import boto3

db = boto3.resource('dynamodb')
table = db.Table("Employees")
response = table.get_item(
    Key = {
        'emp_id':"1"
    }
)
print(response["Item"])
