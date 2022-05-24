import unittest
from unittest.mock import patch
from Demo_Lambda.src.square import lambda_handler  # importing the required modules
from Demo_Lambda.src.square import dynamodb


class test_lambda_handler(unittest.TestCase):
    def setUp(self):
        pass

    @patch('Demo_Lambda.src.square.dynamodb')
    def test_dynamodb_pass(self, mock):
        event = {'productname': 'Johnsons', 'price': '1'}
        mock.return_value = "Success"
        data = lambda_handler(event)
        print(data)
        self.assertEqual(data, "Success")

    @patch('Demo_Lambda.src.square.dynamodb')
    def test_dynamodb_fail(self, mock):
        event = {'productname': 'Jaya', 'price': ''}
        mock.return_value = "Fail"
        output = lambda_handler(event)
        print(output)
        self.assertNotEqual(output, "Failed")
