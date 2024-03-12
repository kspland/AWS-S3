import boto3

#s3 = boto3.resource('s3')

#s3.meta.client.upload_file('')

s3_client = boto3.client('s3')

response = s3_client.upload_file(r'C:\Test\numbers.txt','my-bucket-03112024','numbers.txt')


