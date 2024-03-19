import boto3
from datetime import date

today = date.today()

# format file date as current date mddyyyy
d5 = today.strftime("%#m_%d_%Y")

#s3 = boto3.resource('s3')

#s3.meta.client.upload_file('')

s3_client = boto3.client('s3')

# S3 Test Bucket location
test_bucket = 'lsudatatransfer\importtest\demographic'

# S3 Production Bucket location
prod_bucket = 'lsudatatransfer\import\demographic'

# S3  file path on RHHMS004 for test Demographic file location
test_demo_path = 'E:\StarShare\Test_Demographic\StarRezInbound'

# S3 file path on RHHMS004 for production Demographic file location
prod_demo_path = 'E:\StarShare\Demographic\StarRezInbound'

# Demographic file name is date in format m_dd_YYYY
#  create the file name by running on the date, putting in format and adding .txt
# for the file type
file =  d5 + '.txt'

# create and execute the response
response = s3_client.upload_file(test_demo_path,test_bucket,file)
