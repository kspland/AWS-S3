import boto3

#s3 = boto3.resource('s3')
#s3.neta.client.download_file('mybucket', 'hello.txt', '/tmp/hello.txt')

s3_client = boto3.client('s3')

response =s3_client.download_file('my-bucket-03112024','SampleCurrencyData.txt', r'C:\Test\SampleCurrencyData.txt')

