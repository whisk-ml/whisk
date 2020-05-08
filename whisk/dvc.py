import os
from subprocess import check_output

def pull(dvc_file):
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
