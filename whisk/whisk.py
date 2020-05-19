"""Main module."""
import whisk
from whisk.cli.log_tree import PARENT_TREE_NODE_PREFIX, CHILD_TREE_NODE_PREFIX
from cookiecutter.main import cookiecutter
import os
from os.path import dirname, realpath
# https://docs.python.org/3/library/pathlib.html
# Object-oriented filesystem paths
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def root_module_dir():
    """
    Returns a Path object with the root whisk module directory.
    """
    filepath = realpath(__file__)
    return Path(filepath).parents[0]

def cookiecutter_template_dir():
    return str(root_module_dir() / 'template/')

def project_name_to_slug(project_name):
    """
    Converts a raw project name to a slug:

    * Makes all letters lowercase
    * Replaces spaces with underscores
    """
    return project_name.lower().replace(' ', '_')

def create(project_name, output_dir=".", force=False):
    """
    Creates a whisk project.

    Parameters
    ----------
    project_name : str
        Name of the directory to create for the project. This is converted to a slug via :func:`project_name_to_slug`.

    output_dir : str, optional
        Path to create the directory. Default is the current working directory.

    force : bool, optional
        Recreates the project directory if it exists. Default is `False`.
    """
    # Locks to a specific version as earlier and later versions of whisk could expect a different
    # template structure.
    whisk_version = "whisk=={}".format(whisk.__version__)

    project_name_slug = project_name_to_slug(project_name)

    # `whisk_dependency` is more flexible (for example, specifying a local install)
    # than `whisk_install_requires` and is used in testing to require the local version of whisk.
    extra_content = {
        "project_name": project_name_slug,
        # Added to the project's requirements.txt
        "whisk_dependency": whisk_version,
        # Added to the project's setup.py file
        "whisk_install_requires": whisk_version
    }
    logger.debug("Creating whisk project with extra_content={}".format(extra_content))
    logger.info(PARENT_TREE_NODE_PREFIX+"Creating project directory structure...")
    res = cookiecutter(cookiecutter_template_dir(),
                no_input=True,
                overwrite_if_exists=force,
                output_dir=output_dir,
                extra_context=extra_content)
    logger.info(CHILD_TREE_NODE_PREFIX+"Project created in %s", res)
    logger.info(CHILD_TREE_NODE_PREFIX+"DONE.")
    return res
