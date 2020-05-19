from whisk.project import Project
import whisk.git as git
from whisk.cd import cd
from whisk.cli.log_tree import PARENT_TREE_NODE_PREFIX, CHILD_TREE_NODE_PREFIX
import os
import subprocess
from pathlib import Path
import logging
import sys
from subprocess import PIPE, STDOUT

logger = logging.getLogger(__name__)

NOTEBOOK_EXAMPLE_PATH = "notebooks/getting_started.ipynb"

def log_subprocess_output(logger_with_level,log_lines):
    """
    Calls the logger on each of the log_lines. The log lines are prefixed with :attr:`whisk.cli.log_tree.CHILD_TREE_NODE_PREFIX`.

    Parameters
    ----------
    logger_with_level : Logger
        A logger instance (ex: ``logger.debug``).

    log_lines : str
        A string of log lines separated with ``\\n``.
    """
    for line in log_lines.splitlines(): # b'\n'-separated lines
        logger_with_level(CHILD_TREE_NODE_PREFIX+line)

def exec(desc,cmd):
    """
    Executes the `cmd`, and logs `desc` prior to execution and "DONE" after.
    If the `cmd` has `stdout` or `stderr` output this is logged as well.

    If the exit code is nonzero, raises a ``SystemExit`` execption.

    Parameters
    ----------
    desc : str
        A description of the command operation.

    cmd : str
        The command to execute.
    """
    logger.info(PARENT_TREE_NODE_PREFIX+desc+"...")
    completed_process = None
    try:
        # universal_newlines is the same as `text`. text was added in 3.7:
        # Changed in version 3.7: Added the text parameter, as a more understandable alias of universal_newlines.
        # Added the capture_output parameter.
        completed_process = subprocess.run(cmd, shell=True, check=True, universal_newlines=True, stdout=PIPE, stderr=PIPE)
        log_subprocess_output(logger.info,completed_process.stdout)
        log_subprocess_output(logger.error,completed_process.stderr)
        logger.info(CHILD_TREE_NODE_PREFIX+"DONE.")
    except subprocess.CalledProcessError as e:
        logger.error(CHILD_TREE_NODE_PREFIX+"Error executing `%s`.\n       Stack trace:\n\n", cmd, exc_info=True)
        raise SystemExit("\n###\nSETUP FAILED. See whisk troubleshooting docs for help:\nhttps://whisk.readthedocs.io/en/latest/troubleshooting.html\n###\n")



def exec_setup(nbenv):
    exec("Setting up venv","python3 -m venv {}/venv".format(os.getcwd()))
    exec("Installing Python dependencies via pip  (may take several minutes)","venv/bin/pip install -r requirements.txt > /dev/null")
    logger.info(PARENT_TREE_NODE_PREFIX+"Initializing the Git repo")
    # Idempotent so just execute
    os.system("git init > /dev/null 2>&1")
    logger.info(CHILD_TREE_NODE_PREFIX+"DONE.")
    # Would rather use --sys-prefix, but not working:
    # https://github.com/jupyter/notebook/issues/4567
    exec("Setting up kernel={} for Jupyter Notebooks".format(nbenv),"venv/bin/python -m ipykernel install --user --name={}".format(nbenv))
    set_example_notebook_kernel(nbenv)
    # direnv will fail if not installed
    os.system("cp .envrc.example .envrc")
    os.system("direnv allow . > /dev/null 2>&1")
    if git.has_unstaged_changes():
        exec("Adding files to git", "git add .")
        exec("Making initial Git commit", "git commit -m 'Initial project structure' --author=\"Whisk <whisk@whisk-ml.org>\" > /dev/null")

def set_example_notebook_kernel(nbenv):
    """
    Updates the :attr:`NOTEBOOK_EXAMPLE_PATH` notebook kernel to use the kernel with name ``nbenv``.
    """
    nb_file = Path(NOTEBOOK_EXAMPLE_PATH)
    if not nb_file.is_file():
        logger.info("Getting started notebook does not exist @ {}. Not applying venv.".format(nb_file))
        return
    # Read in the file
    with open(NOTEBOOK_EXAMPLE_PATH, 'r') as file :
      filedata = file.read()

    # This could be run after the initial cookiecutter install.
    filedata = filedata.replace("{{cookiecutter.project_name}}", nbenv)

    # Write the file out again
    with open(NOTEBOOK_EXAMPLE_PATH, 'w') as file:
        file.write(filedata)

def log_success(dir):
    """Logs that the setup completed successfully and provides next steps."""
    logger.info("│\n└── Setup completed.")
    logger.info("\n###\nYOUR PROJECT IS READY. See the docs for help: https://whisk.readthedocs.io\n")
    logger.info("Get started:\n")
    if os.getcwd() != dir:
        # If not in the project directory, instruct the user to cd into the project.
        logger.info("cd %s", dir)
    logger.info("source venv/bin/activate")
    logger.info("###\n")

def log_pip_freeze():
    """Logs the output of ``pip freeze`` at the debug level."""
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'], universal_newlines=True)
    logger.debug("pip freeze output:\n"+reqs)

def setup(dir):
    """
    Sets up the project environment.

    Setup performs the following actions after changing the working directory to ``dir``:

    * Creates a `Python3 venv <https://docs.python.org/3/library/venv.html />`_ named "venv"
    * Installs the dependencies listed in the project's requirements.txt.
    * Initializes a Git repo
    * Creates an iPython kernel for use in Jupyter notebooks with name = <project_name>.
    * Creates a ``.envrc`` file based on ``.envrc.example`` for use with `direnv <https://github.com/direnv/direnv />`_.
      direnv loads environment variables listed in ``.envrc`` into the shell and is also used to auto-activate and
      deactivate the venv when entering and exiting the project directory.
    * Calls ``direnv allow .`` so the ``.envrc`` file can be loaded.
    * Makes an initial Git commit

    Parameters
    ----------
    dir : str
        The full path to the project directory.
    """
    project = Project(dir)
    project.validate_in_project()
    nbenv = project.name
    with cd(dir):
        logger.debug("cwd={}".format(os.getcwd()))
        exec_setup(nbenv)
    log_success(dir)
    log_pip_freeze()
