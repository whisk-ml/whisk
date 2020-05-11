import click
from whisk.project import Project
import os
from subprocess import call
project = Project()

@click.group()
def cli():
    pass

@cli.command()
@click.option("--bucket", default="whisk-" + project.name.replace("_","-"), show_default=True)
def remote_add(bucket):
    """
    Adds a DVC S3 remote as the default remote using the provided S3 bucket.
    """
    call("dvc remote add -d s3 s3://{}/".format(bucket), shell=True)

@cli.command()
@click.option("--name", default="s3", show_default=True)
def remote_remove(name):
    """
    Removes the DVC S3 remote.
    """
    call("dvc remote remove {}".format(name), shell=True)

@cli.command()
def setup():
    """
    Initializes dvc, adds a local remote, and installs git post-checkout hooks.

    Run `dvc destroy` to revert.
    """
    if os.system("venv/bin/dvc status > /dev/null 2>&1") != 0:
        # Initializing DVC
        call("venv/bin/dvc init > /dev/null", shell=True)
        # Setting up default local DVC remote
        call("venv/bin/dvc remote add -d local /tmp/dvc-storage", shell=True)
    if not os.path.isfile(".git/hooks/post-checkout"):
        # Installing Git hooks into the DVC repository
        call("venv/bin/dvc install > /dev/null", shell=True)
