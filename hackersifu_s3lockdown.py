import boto3
import json
import sys

def lambda_handler(event, context):
    # The following code is designed to be invoked through a CloudWatch rule.
    s3 = boto3.resource('s3')
    client = boto3.client('s3')
    for bucket in s3.buckets.all():
      print(bucket.name)
    for bucket in s3.buckets.all():
      response = client.put_public_access_block(
          Bucket=bucket.name,
          PublicAccessBlockConfiguration={
              'BlockPublicAcls': True,
              'IgnorePublicAcls': True,
              'BlockPublicPolicy': True,
              'RestrictPublicBuckets': True
    }
)

    return {
        'statusCode': 200,
        'body': json.dumps('Your buckets are secure from the hacks!')
    
    }
    sys.exit()