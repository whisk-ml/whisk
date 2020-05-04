#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import getopt
import fileinput
import subprocess

LONG_OPTIONS = ["nbenv="]
NOTEBOOK_EXAMPLE_PATH = "notebooks/example.ipynb"

def parse_arguments(full_cmd_arguments):
    # Keep all but the first
    argument_list = full_cmd_arguments[1:]

    try:
        arguments, values = getopt.getopt(argument_list, "", LONG_OPTIONS)
    except getopt.error as err:
        # Output error, and return with an error code
        print (str(err))
        sys.exit(2)

    return arguments, values

def set_nbenv(arguments):
    nbenv = 'venv'
    for current_argument, current_value in arguments:
        if current_argument in ("--nbenv"):
            nbenv = current_value
    return nbenv

def exec(desc,cmd):
    """
    Executes the `cmd`, and prints `desc` prior to execution.
    If the exit code is nonzero, raises a `SystemExit` execption.
    """
    print(desc+"...", end="", flush=True)
    exit_code = subprocess.call(cmd, shell=True)
    if exit_code == 0:
        print("✓")
    else:
        print("⚠️  (exit code= {})".format(exit_code))
        raise SystemExit("💣 Aborting install. An error occurred running the install script.")

def exec_setup(nbenv):
    exec("Setting up venv","python3 -m venv {}/venv".format(os.getcwd()))
    exec("Installing Python dependencies via pip","venv/bin/pip install -r requirements.txt > /dev/null")
    print("Initializing the Git repo")
    # Idempotent so just execute
    os.system("git init > /dev/null 2>&1")
    if os.system("venv/bin/dvc status > /dev/null 2>&1") != 0:
        exec("Initializing DVC","venv/bin/dvc init > /dev/null")
        exec("Setting up default local DVC remote","venv/bin/dvc remote add -d local /tmp/dvc-storage")
    if not os.path.isfile(".git/hooks/post-checkout"):
        exec("Installing Git hooks into the DVC repository","venv/bin/dvc install > /dev/null")
    # Would rather use --sys-prefix, but not working:
    # https://github.com/jupyter/notebook/issues/4567
    exec("Setting up venv={} for Jupyter Notebooks".format(nbenv),"venv/bin/python -m ipykernel install --user --name={}".format(nbenv))
    set_example_notebook_kernel(nbenv)
    # direnv will fail if not installed
    os.system("cp .envrc.example .envrc")
    os.system("direnv allow . > /dev/null 2>&1")

def set_example_notebook_kernel(nbenv):
    # Read in the file
    with open(NOTEBOOK_EXAMPLE_PATH, 'r') as file :
      filedata = file.read()

    # Replace the target string
    filedata = filedata.replace("[PROJECT_NAME]", nbenv)

    # Write the file out again
    with open(NOTEBOOK_EXAMPLE_PATH, 'w') as file:
        file.write(filedata)

if __name__ == "__main__":
    arguments, values = parse_arguments(sys.argv)
    nbenv = set_nbenv(arguments)
    exec_setup(nbenv)
    print("Install completed ✓.")
