import os
from dotenv import load_dotenv
import boto3


def get_variables():
    bucket, folder = get_env()
    filenames = get_filenames(bucket, folder)
    return bucket, folder, filenames


def get_env() -> tuple:
    load_dotenv()
    bucket = os.getenv('BUCKET_NAME')
    folder = os.getenv('FOLDER_NAME')
    return bucket, folder


def get_filenames(bucket, folder) -> list:
    s3 = boto3.resource("s3")
    s3_bucket = s3.Bucket(bucket)
    files = [f.key.split(folder + "/")[1]
             for f in s3_bucket.objects.filter(Prefix=folder).all()]
    if files[0] == '':
        del files[0]
    return files
