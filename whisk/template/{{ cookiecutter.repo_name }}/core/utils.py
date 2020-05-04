import os
from subprocess import check_output
from os.path import dirname, realpath
from pathlib import Path

def dvc_pull(dvc_file):
    """
    Pulls the output of the specified `dvc_file` into the repository.
    This is useful when running outside the local environment (like a deployed web server)
    that doesn't have all data files by default.

    If `dvc pull` fails (has a non-zero exit status), a `subprocess.CalledProcessError` exception
    is raised.
    """
    # The deployed app isn't a git repo but needs to be for dvc.
    # `git init` is idempotent.
    os.system("git init")
    # Pull the training output (the serialized model) when running on a deployed server.
    check_output(["dvc", "pull", dvc_file])

def project_dir():
    """
    Returns a string w/the full path to root project directory.
    """
    filepath = realpath(__file__)
    dir_of_file = dirname(filepath)
    parent_dir_of_file = dirname(dir_of_file)
    return parent_dir_of_file

def project_dir_name():
    """
    Returns a string w/the name of the project directory.
    """
    p = Path(project_dir())
    return p.name
