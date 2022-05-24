demo_lambda.py



def lambda_handler(event):
logging.info('Lambda Handler Triggered')
if event is not None:
address_name = event['Address']
return create_dynamoDB(address_name)




def create_dynamoDB(address):
logging.info('create_dynamoDB method called')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Contact')
try:
response = table.put_item(
Item={
'Address': address
}
)
print('Response: ', response)
return 'Success'
except Exception as e:
logging.error('Error occured with Exception')
return e





test_demo_lambda part




# import necessary files
import pytest



from demo_lambda.src.demo_lambda import lambda_handler




def test_lambda_handler_successful(mocker):
event = {'Address': 'Gurgaon'}
mocker.patch('demo_lambda.src.demo_lambda.create_dynamoDB', return_value='Success')
response = lambda_handler(event)
assert response == 'Success'



def test_lambda_handler_unsuccessful(mocker):
event = {'Address': 'Gurgaon'}
mocker.patch('demo_lambda.src.demo_lambda.create_dynamoDB', return_value='Fail')
response = lambda_handler(event)
assert response != 'Success'