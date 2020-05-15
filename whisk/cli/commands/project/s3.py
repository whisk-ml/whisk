import click
import json
import boto3
import botocore
from whisk.project import Project

project = Project()
"""A reference to the associated :class:`whisk.project.Project` object for this project."""

PUBLIC_READ_ONLY_POLICY = {
  "Version":"2012-10-17",
  "Statement":[
    {
      "Sid":"PublicRead",
      "Effect":"Allow",
      "Principal": "*",
      "Action":["s3:GetObject"],
      "Resource":["arn:aws:s3:::[BUCKET_NAME]/*"]
    }
  ]
}
"""The public read-only policy to apply to an S3 bucket."""

DEFAULT_BUCKET_NAME = "whisk-" + project.name.replace("_","-")
"""The default bucket name for the project."""

S3_CLIENT = boto3.client('s3')

@click.group()
def cli():
    pass

@cli.command()
@click.option("--bucket", default=DEFAULT_BUCKET_NAME, show_default=True)
def create(bucket):
    """
    Creates an S3 bucket to store data. If no bucket name is provided, the bucket name is generated from the project directory name.
    """
    S3_CLIENT.create_bucket(Bucket=bucket)
    click.echo("{} S3 bucket created.".format(bucket))

@cli.command()
@click.option("--bucket", default=DEFAULT_BUCKET_NAME, show_default=True)
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
    S3_CLIENT.delete_bucket(Bucket=bucket)
    click.echo("{} S3 bucket deleted.".format(bucket))

@cli.command()
@click.option("--bucket", default=DEFAULT_BUCKET_NAME, show_default=True)
def make_public(bucket):
    """
    Creates a public read-only policy for the S3 bucket.

    This is useful when end users need access to data or artifacts not stored in the code version control.

    Use ``whisk delete-policy`` to revert.
    """
    policy = PUBLIC_READ_ONLY_POLICY
    S3_CLIENT.put_bucket_policy(Bucket=bucket, Policy=json.dumps(policy).replace("[BUCKET_NAME]",bucket))
    click.echo("{} S3 bucket is now read-only to the public.".format(bucket))

@cli.command()
@click.option("--bucket", default=DEFAULT_BUCKET_NAME, show_default=True)
def delete_policy(bucket):
    """
    Deletes the policy associated with the S3 bucket.
    """
    S3_CLIENT.delete_bucket_policy(Bucket=bucket)
    click.echo("{} S3 bucket deleted.".format(bucket))
