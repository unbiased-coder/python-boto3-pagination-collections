import boto3_helper

def boto3_s3_list_files_using_pagination():
    session = boto3_helper.init_aws_session()
    s3 = session.client('s3')
    
    paginator = s3.get_paginator('list_objects')
    page_iterator = paginator.paginate(Bucket='unbiased-coder-test-bucket')

    search_criteria = 'Contents[?Size > `500`][]'
    filtered_iterator = page_iterator.search(search_criteria)
    
    for s3_obj in filtered_iterator:
        print ('File: ', s3_obj['Key'], 'with Size: ', s3_obj['Size'])

boto3_s3_list_files_using_pagination()
