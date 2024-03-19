import boto3

#s3 = boto3.resource('s3')
#s3.neta.client.download_file('mybucket','hello.txt','/tmp/hello.txt')

s3_client = boto3.client('s3')

bucket = 'lsudatatransfer'

file = 'StarRezS3Test.txt'

path = r'E:\StarShare\S3-TestLocation\StarRezS3Test.txt'



response = s3_client.download_file(bucket,file,path)

#response = s3_client.download_file('lsudatatransfer','StarRezS3Test.txt', r'E:\StarShare\S3-TestLocation\StarRezS3Test.txt')
