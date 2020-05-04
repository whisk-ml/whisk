from invoke import task
import boto3
from core.utils import project_dir_name

@task(help={'bucket': "The name of the S3 bucket to destroy. If not provided, this is generated from the project directory name."})
def delete(c, bucket=None):
    """
    Delete the S3 bucket used for data storage.
    """
    if bucket == None:
        bucket = "dvc-" + project_dir_name().replace("_","-")
    bucket_resource = boto3.resource('s3').Bucket(bucket)
    bucket_resource.objects.all().delete()
    s3 = boto3.client("s3")
    s3.delete_bucket(Bucket=bucket)

@task(help={'bucket': "The name of the S3 bucket to use for the DVC remote. If not provided, this is generated from the project directory name."})
def dvc(c, bucket=None):
    """
    Removes the DVC S3 remote.
    """
    if bucket == None:
        bucket = "dvc-" + project_dir_name().replace("_","-")
    c.run("dvc remote remove s3".format(bucket))
