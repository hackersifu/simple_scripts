import os
import boto3
import logging
import time
import json
import datetime


logger = logging.getLogger()
logger.setLevel(logging.INFO)
current_date = datetime.datetime.now()
current_date_string = str(current_date)

# List functions in a region
def list_functions():
    """Function to list all the Lambda functions in a region"""
    lambda_client = boto3.client('lambda')
    cloudwatch_client = boto3.client('logs')
    response = lambda_client.list_functions()
    print(response)
    functions = []
    for function in response['Functions']:
        functions.append(function['FunctionName'])
    print(functions)
    # Take the functions and perform GetFunction on each
    for function in functions:
        print(function)
        logging.info("Function: " + function + " is being reviewed")
        response = lambda_client.get_function(
            FunctionName=function
        )
        print(response)
        # Print the function's log group
        logging.info("Function: " + function + " is in log group: " + response['Configuration']['LoggingConfig']['LogGroup'])
        log_group_name = response['Configuration']['LoggingConfig']['LogGroup']
        # Use the log_group_name to get the log events
        response2 = cloudwatch_client.describe_log_streams(
            logGroupName=log_group_name,
            orderBy='LastEventTime',
            descending=True
        )
        logging.info("Printing results from describe_log_streams")
        logging.info(" ")
        time.sleep(2)
        print(response2)
        time.sleep(1)
    return functions

def lambda_handler(event, context):
    list_functions()

if __name__ == '__main__':
    lambda_handler(None, None)
