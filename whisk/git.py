from subprocess import check_output

def has_unstaged_changes():
    """Returns True if the git repo in the current directory has unstaged changes."""
    res=check_output("git status --porcelain",shell=True, universal_newlines=True)
    return ("\n" in res)
