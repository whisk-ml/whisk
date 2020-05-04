from invoke import task
import boto3
from core.utils import project_dir_name

@task(help={'bucket': "The name of the S3 bucket to use. If not provided, this is generated from the project directory name."})
def create(c, bucket=None):
    """
    Creates an S3 bucket to store data.
    """
    if bucket == None:
        bucket = "dvc-" + project_dir_name().replace("_","-")
    s3 = boto3.client("s3")
    s3.create_bucket(Bucket=bucket)

@task(pre=[create],help={'bucket': "The name of the S3 bucket to use for the DVC remote. If not provided, this is generated from the project directory name."})
def dvc(c, bucket=None):
    """
    Adds a DVC S3 remote as the default remote and creates the S3 bucket.
    """
    if bucket == None:
        bucket = "dvc-" + project_dir_name().replace("_","-")
    c.run("dvc remote add -d s3 s3://{}/".format(bucket))
