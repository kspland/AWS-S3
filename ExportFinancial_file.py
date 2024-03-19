import boto3
from datetime import date

today = date.today()

# format file date as current date YYYYmmdd
d1 = today.strftime("%Y%m%d")

#s3 = boto3.resource('s3')
#s3.neta.client.download_file('mybucket','hello.txt','/tmp/hello.txt')

test_bucket = 'lsudatatransfer\exporttest\financialexport'

prod_bucket = 'lsudatatransfer\export\financialexport'

test_fin_path = 'E:\StarShare\Financial\StarRezOutbound'

prod_fin_path = 'E:\StarShare\Test_Financial\StarRezOutbound'

# File format is FiancialExport_YYYYmmdd
# Example is FianancialExport_20240318.txt
file = 'FinancialExport_' + d1 + '.txt'


response = s3_client.download_file(test_bucket,file,test_fin_path)

