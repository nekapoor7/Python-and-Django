import boto3

db = boto3.resource('dynamodb')
table = db.Table("Employees")
table.put_item(
    Item={
    'emp_id':"2",
    'name':"Harsh",
    'Age' :"33"
}
)
