import click
import sys
import subprocess
from whisk.project import Project

@click.group()
def cli():
    pass

@cli.command()
@click.argument('relative_path')
def run(relative_path):
    """
    Run a notebook from the command line with the given RELATIVE_PATH.
    """
    project = Project()
    subprocess.call("jupyter nbconvert --clear-output --ExecutePreprocessor.timeout=1000 --execute {}".format(relative_path),shell=True)
