import boto3
from datetime import date

today = date.today()

# format file date as current date mddyyyy
d5 = today.strftime("%#m_%d_%Y")

#s3 = boto3.resource('s3')

#s3.meta.client.upload_file('')

s3_client = boto3.client('s3')

# S3 Bucket
bucket = 'lsudatatransfer'


# Demographic file name is date in format m_dd_YYYY
# create the file name getting the date code executes and put in format add .txt for file type
# Example file name 3_26_2024   or 6_2_2024
file =   d5 + '.txt'

# S3  file path on RHHMS004 for test Demographic file location
test_demo_path = 'E:\\StarShare\\Test_Demographic\\StarRezInbound\\' + file

# S3 file path on RHHMS004 for production Demographic file location
#prod_demo_path = 'E:\\StarShare\\Demographic\\StarRezInbound\\' + file


# To access the folder within the bucket place add the folder path to the file name
filebase = 'import/demographic/' + file

# used to execute during testingresponse = s3_client.upload_file(test_demo_path,test_bucket,file)

# create and execute the response

response = s3_client.upload_file(test_demo_path,bucket,filebase)
