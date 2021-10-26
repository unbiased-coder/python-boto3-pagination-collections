import boto3_helper

def boto3_s3_list_files_using_pagination():
    page_size = 3
    session = boto3_helper.init_aws_session()
    s3 = session.client('s3')
    
    paginator = s3.get_paginator('list_objects')
    page_iterator = paginator.paginate(Bucket='unbiased-coder-test-bucket', PaginationConfig={'PageSize': page_size})
    
    print ('Fetching results using PAGE SIZE: ', page_size)
    
    for page in page_iterator:
        contents = page['Contents']
        print ('Received number of results: ', len(contents))
        for s3_obj in contents:
            print (s3_obj)

boto3_s3_list_files_using_pagination()
