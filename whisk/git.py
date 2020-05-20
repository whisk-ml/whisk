from subprocess import check_output
from pathlib import Path
import os


def is_repo(dir=os.getcwd()):
    """
    Returns ``True`` if the ``dir`` is a git repo.

    Parameters
    ----------
    dir : str
        A path to a directory.
    """
    return (Path(dir) / '.git').exists()


def has_unstaged_changes(dir=os.getcwd()):
    """
    Returns ``True`` if the git repo in the directory
    has unstaged changes.
    """
    res = check_output("git status --porcelain", shell=True,
                       cwd=dir,
                       universal_newlines=True)
    return ("\n" in res)
