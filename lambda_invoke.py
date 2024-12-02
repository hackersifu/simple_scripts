import boto3
from datetime import datetime

# List of regions. Recommend to modify.
region_list = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']

def get_lambda_first_invocation_time(function_name, aws_region, lookback_days):
    """Function to get the last invocation time for each Lambda function."""
    logs_client = boto3.client('logs', region_name=aws_region)
    try:
        log_group_name = f"/aws/lambda/{function_name}"
        start_time = int((datetime.now().timestamp() - (lookback_days * 86400)) * 1000)
        response = logs_client.filter_log_events(
            logGroupName=log_group_name,
            limit=1,
            startTime=start_time, 
            interleaved=True
        )
        
        if response['events']:
            first_invocation_time = response['events'][0]['timestamp']
            return datetime.utcfromtimestamp(first_invocation_time / 1000).strftime('%Y-%m-%d %H:%M:%S')
        else:
            return f"No recent invocations (looking back {lookback_days} days)"
    
    except logs_client.exceptions.ResourceNotFoundException:
        return "No logs available"

def list_lambda_functions(aws_region, lookback_days):
    """Function to list all Lambda functions."""
    lambda_client = boto3.client('lambda', region_name=aws_region)
    paginator = lambda_client.get_paginator('list_functions')
    response_iterator = paginator.paginate()

    lambda_functions = []

    for page in response_iterator:
        for function in page['Functions']:
            function_name = function['FunctionName']
            first_invocation_time = get_lambda_first_invocation_time(function_name, aws_region, lookback_days)
            lambda_functions.append({
                'FunctionName': function_name,
                'FirstInvocationTime': first_invocation_time,
                'Region': aws_region
            })
    
    return lambda_functions

def main():
    """Main function to run subsequent functions."""
    while True:
        try:
            lookback_days = int(input("Enter the number of days to look back for Lambda invocations (default is 30): ") or 30)
            if lookback_days < 0:
                raise ValueError("The lookback period cannot be negative.")
            break
        except ValueError as error:
            print(f"Invalid input: {error}. Please enter a positive integer.")

    all_lambda_functions = []
    for aws_region in region_list:
        lambda_functions = list_lambda_functions(aws_region, lookback_days)
        all_lambda_functions.extend(lambda_functions)

    print(f"{'FunctionName':<50}{'FirstInvocationTime':<30}{'Region'}")
    print("-" * 90)

    for function in all_lambda_functions:
        print(f"{function['FunctionName']:<50}{function['FirstInvocationTime']:<30}{function['Region']}")

if __name__ == '__main__':
    main()
