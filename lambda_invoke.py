import boto3
from datetime import datetime

# Define the list of regions
region_list = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']

def get_lambda_last_invocation_time(function_name, aws_region):
    logs_client = boto3.client('logs', region_name=aws_region)
    try:
        # Get the function's CloudWatch log group
        log_group_name = f"/aws/lambda/{function_name}"
        
        # Use filter_log_events to find the last log event for the function
        response = logs_client.filter_log_events(
            logGroupName=log_group_name,
            limit=1,
            startTime=int((datetime.now().timestamp() - (30 * 86400)) * 1000),  # Looks back 30 days
            interleaved=True
        )
        
        if response['events']:
            last_invocation_time = response['events'][0]['timestamp']
            return datetime.utcfromtimestamp(last_invocation_time / 1000).strftime('%Y-%m-%d %H:%M:%S')
        else:
            return "No recent invocations (looking back 30 days)"
    
    except logs_client.exceptions.ResourceNotFoundException:
        return "No logs available"

def list_lambda_functions(aws_region):
    lambda_client = boto3.client('lambda', region_name=aws_region)
    paginator = lambda_client.get_paginator('list_functions')
    response_iterator = paginator.paginate()

    lambda_functions = []

    for page in response_iterator:
        for function in page['Functions']:
            function_name = function['FunctionName']
            last_invocation_time = get_lambda_last_invocation_time(function_name, aws_region)
            lambda_functions.append({
                'FunctionName': function_name,
                'LastInvocationTime': last_invocation_time,
                'Region': aws_region
            })
    
    return lambda_functions

def main():
    # To store all Lambda functions across regions
    all_lambda_functions = []
    
    # Iterate over each region
    for aws_region in region_list:
        lambda_functions = list_lambda_functions(aws_region)
        all_lambda_functions.extend(lambda_functions)

    # Print the header
    print(f"{'FunctionName':<50}{'LastInvocationTime':<30}{'Region'}")
    print("-" * 90)

    # Print each Lambda function's details
    for function in all_lambda_functions:
        print(f"{function['FunctionName']:<50}{function['LastInvocationTime']:<30}{function['Region']}")

if __name__ == '__main__':
    main()
