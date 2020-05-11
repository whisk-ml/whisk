import click
import boto3
import botocore
from whisk.project import Project

project = Project()

@click.group()
def cli():
    pass

@cli.command()
@click.option("--bucket", default="whisk-" + project.name.replace("_","-"), show_default=True)
def create(bucket):
    """
    Creates an S3 bucket to store data. If no bucket name is provided, the bucket name is generated from the project directory name.
    """
    s3 = boto3.client("s3")
    s3.create_bucket(Bucket=bucket)
    click.echo("{} S3 bucket created.".format(bucket))

@cli.command()
@click.option("--bucket", default="whisk-" + project.name.replace("_","-"), show_default=True)
def delete(bucket):
    """
    Delete the S3 bucket used for data storage. If no bucket name is provided, the bucket name is generated from the project directory name.
    """
    bucket_resource = boto3.resource('s3').Bucket(bucket)
    try:
        bucket_resource.objects.all().delete()
    except Exception as e:
        click.echo("Unable to delete S3 bucket with name={}.\nError={}".format(bucket,e))
        exit(1)
    s3 = boto3.client("s3")
    s3.delete_bucket(Bucket=bucket)
    click.echo("{} S3 bucket deleted.".format(bucket))
