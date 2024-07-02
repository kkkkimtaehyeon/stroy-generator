from fastapi import UploadFile
import boto3
import os
import uuid
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
BUCKET = os.getenv('AWS_S3_BUCKET')
REGION = os.getenv('AWS_S3_REGION')

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

def upload_image_on_s3(image_file: UploadFile):
    key = get_object_key(image_file)
    content_type = image_file.content_type  # 파일의 ContentType을 가져옵니다.
    #file_content = image_file.read()
    s3.put_object(Body=image_file.file, Bucket=BUCKET, Key=key, ContentType=content_type)
    return f'https://{BUCKET}.s3.{REGION}.amazonaws.com/{key}'

def get_object_key(file):
    return str(uuid.uuid4()) + "_" + file.filename

def delete_image_on_s3(key: str):
    # TODO s3에서 이미지 삭제
    pass