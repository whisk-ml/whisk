from invoke import task
import sys
import subprocess

@task(help={"relative_path": "Relative path to the notebook"})
def run(c, relative_path):
    """
    Run a notebook from the command line.
    """
    c.run("jupyter nbconvert --clear-output --ExecutePreprocessor.timeout=1000 --execute {}".format(relative_path))
    sys.stdout.flush()
