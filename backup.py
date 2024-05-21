import boto3
import logging
import datetime
import subprocess
import os

date = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.info("Starting backup")

username = os.getenv('user')
password = os.getenv('password')
hostname = os.getenv('host')
port = os.getenv('port', '5432')
database = os.getenv('db')

file_name = f"{os.getenv('prefix', 'psql')}_{date}.sql.gz"

os.environ['PGPASSWORD'] = password
command = f"pg_dump -Z 9 -v -h {hostname} -p {port} -U {username} -d {database} > {file_name}"
subprocess.run(command, shell=True, check=True)

logging.info("Connecting to S3")
bucket = os.getenv('bucket')
aws_access_key_id = os.getenv('access_key_id')
aws_secret_access_key = os.getenv('access_key')
endpoint_url = os.getenv('endpoint')
expires = os.getenv('expires', '+168h')  # Default 7 days

s3_client = boto3.client(
    "s3",
    endpoint_url=endpoint_url,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)

logging.info("Uploading to S3")
s3_client.upload_file(Filename=file_name, Bucket=bucket, Key=file_name, ExtraArgs={
    'Metadata': {
        'Object-Expires': expires
    }
})

logging.info("Removing local")
os.remove(file_name)
logging.info("Finished")
