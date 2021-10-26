import sys
import boto3_helper

def boto3_s3_list_files_using_collections():
    page_size = 3
    session = boto3_helper.init_aws_session()
    s3 = session.resource('s3')
    bucket = s3.Bucket(name='unbiased-coder-test-bucket')
    print ('Fetching results using PAGE SIZE: ', page_size)
    for s3_file in bucket.objects.page_size(page_size):
        print ('S3 file', s3_file)

boto3_s3_list_files_using_collections()
