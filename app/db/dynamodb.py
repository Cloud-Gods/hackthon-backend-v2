import boto3
from app.core.config import settings

dynamodb = boto3.resource(
    'dynamodb',
    region_name=settings.aws_region,
    aws_access_key_id=settings.aws_access_key_id,
    aws_secret_access_key=settings.aws_secret_access_key
)

def get_procesos_table():
    return dynamodb.Table(settings.dynamodb_table_procesos)
