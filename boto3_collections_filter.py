import sys
import boto3_helper

def boto3_s3_list_files_using_collections():
    session = boto3_helper.init_aws_session()
    s3 = session.resource('s3')
    bucket = s3.Bucket(name='unbiased-coder-test-bucket')
    for s3_file in bucket.objects.all():
        if s3_file.size > 500:
            print ('S3 file', s3_file)

boto3_s3_list_files_using_collections()
