import boto3


def lambda_handler(event):
    if event is None:
        print("Empty")
    else:
        productname = event['productname']
        price = event['price']
    return dynamodb(productname, price)


def dynamodb(productname, price):
    dynamodb = boto3.resource('dynamodb')
    try:
        dynamo = dynamodb.Table('Products')
        dynamo.put_key(
            Key={
                'Productname': productname, 'Price': price
            }
        )
        return "Successful"
    except Exception:
        print("Invalid")
