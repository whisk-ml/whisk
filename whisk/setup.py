from whisk.project import Project
import whisk.git as git
from whisk.cd import cd
from whisk.cli.log_tree import PARENT_TREE_NODE_PREFIX, CHILD_TREE_NODE_PREFIX
import os
import subprocess
from pathlib import Path
import logging
import sys
from subprocess import PIPE

logger = logging.getLogger(__name__)

NOTEBOOK_EXAMPLE_PATH = "notebooks/getting_started.ipynb"


def log_subprocess_output(logger_with_level, log_lines):
    """
    Calls the logger on each of the log_lines. The log lines are prefixed with
    :attr:`whisk.cli.log_tree.CHILD_TREE_NODE_PREFIX`.

    Parameters
    ----------
    logger_with_level : Logger
        A logger instance (ex: ``logger.debug``).

    log_lines : str
        A string of log lines separated with ``\\n``.
    """
    for line in log_lines.splitlines():  # b'\n'-separated lines
        logger_with_level(CHILD_TREE_NODE_PREFIX+line)


def exec(desc, cmd):
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
        # Changed in version 3.7: Added the text parameter, as a more
        # understandable alias of universal_newlines.
        # Added the capture_output parameter.
        completed_process = subprocess.run(cmd, shell=True, check=True,
                                           universal_newlines=True,
                                           stdout=PIPE,
                                           stderr=PIPE)
        log_subprocess_output(logger.info, completed_process.stdout)
        log_subprocess_output(logger.error, completed_process.stderr)
        logger.info(CHILD_TREE_NODE_PREFIX+"DONE.")
    except subprocess.CalledProcessError:
        logger.error(CHILD_TREE_NODE_PREFIX +
                     "Error executing `%s`.\n       Stack trace:\n\n",
                     cmd, exc_info=True)
        raise SystemExit("""

###
SETUP FAILED. See whisk troubleshooting docs for help:
https://docs.whisk-ml.org/en/latest/troubleshooting.html
###

        """)

def init_git_repo():
    logger.info(PARENT_TREE_NODE_PREFIX+"Initializing the Git repo")
    # Idempotent so ok to execute
    os.system("git init > /dev/null 2>&1")
    logger.info(CHILD_TREE_NODE_PREFIX+"DONE.")

def init_direnv():
    os.system("cp .envrc.example .envrc")
    # direnv command will fail if not installed ... just ignore
    os.system("direnv allow . > /dev/null 2>&1")

def exec_setup(project):
    """
    Sets up an environment for the given project.

    Parameters
    ----------
    project : whisk.project.Project
        A whisk project.
    """
    exec("Setting up venv", "python3 -m venv {}/venv".format(project.dir))

    exec("Installing Python dependencies via pip  (may take several minutes)",
         "venv/bin/pip install -r requirements.txt > /dev/null")

    logger.info(PARENT_TREE_NODE_PREFIX+"Checking if a git repo has been initialized...")
    is_git_repo = project.is_git_repo()
    logger.info(CHILD_TREE_NODE_PREFIX+str(is_git_repo))
    if not is_git_repo:
        init_git_repo()

    # Would rather use --sys-prefix, but not working:
    # https://github.com/jupyter/notebook/issues/4567
    nbenv = project.name
    exec("Setting up kernel={} for Jupyter Notebooks".format(nbenv),
         "venv/bin/python -m ipykernel install --user --name={}".format(nbenv))
    set_example_notebook_kernel(nbenv)

    init_direnv()

    if not is_git_repo and git.has_unstaged_changes():
        exec("Adding files to git", "git add .")
        exec("Making initial Git commit",
             "git commit -m 'Initial project structure' --author=\"Whisk <whisk@whisk-ml.org>\" > /dev/null")

def notebook_exists(notebook_path):
    logger.debug("Checking if notebook exists at path={}".format(notebook_path))
    nb_file = Path(NOTEBOOK_EXAMPLE_PATH)
    return nb_file.is_file()

def set_example_notebook_kernel(nbenv):
    """
    Updates the :attr:`NOTEBOOK_EXAMPLE_PATH` notebook kernel to use
    the kernel with name ``nbenv``.
    """
    if not notebook_exists(NOTEBOOK_EXAMPLE_PATH):
        logger.info(
            f"Getting started notebook does not exist @ {NOTEBOOK_EXAMPLE_PATH}. Not applying venv."
        )
        return
    # Read in the file
    with open(NOTEBOOK_EXAMPLE_PATH, 'r') as file:
        filedata = file.read()

    # This could be run after the initial cookiecutter install.
    filedata = filedata.replace("{{cookiecutter.project_name}}", nbenv)

    # Write the file out again
    with open(NOTEBOOK_EXAMPLE_PATH, 'w') as file:
        file.write(filedata)


def log_success(dir):
    """Logs that the setup completed successfully and provides next steps."""
    logger.info("│\n└── Setup completed.")
    logger.info("""

###
YOUR PROJECT IS READY. See the docs for help: https://docs.whisk-ml.org

Get started:
    """)
    if os.getcwd() != dir:
        # If not in the project directory,
        # instruct the user to cd into the project.
        logger.info("cd %s", dir)
    logger.info("source venv/bin/activate")
    if notebook_exists(Path(dir) / NOTEBOOK_EXAMPLE_PATH):
        logger.info(f"jupyter-notebook {NOTEBOOK_EXAMPLE_PATH}")
    logger.info("###\n")


def log_pip_freeze():
    """Logs the output of ``pip freeze`` at the debug level."""
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'],
                                   universal_newlines=True)
    logger.debug("pip freeze output:\n"+reqs)


def setup(dir):
    """
    Sets up the project environment.

    Setup performs the following actions after changing the working
    directory to ``dir``:

    * Creates a `Python3 venv <https://docs.python.org/3/library/venv.html />`_
      named "venv"
    * Installs the dependencies listed in the project's requirements.txt.
    * Initializes a Git repo
    * Creates an iPython kernel for use in Jupyter notebooks with
      name = <project_name>.
    * Creates a ``.envrc`` file based on ``.envrc.example`` for use with
      `direnv <https://github.com/direnv/direnv />`_. direnv loads environment
      variables listed in ``.envrc`` into the shell and is also used to
      auto-activate and deactivate the venv when entering and exiting the
      project directory.
    * Calls ``direnv allow .`` so the ``.envrc`` file can be loaded.
    * Makes an initial Git commit

    Parameters
    ----------
    dir : str
        The full path to the project directory.
    """
    project = Project(dir)
    project.validate_in_project()
    with cd(dir):
        logger.debug("cwd={}".format(os.getcwd()))
        exec_setup(project)
    log_success(dir)
    log_pip_freeze()
