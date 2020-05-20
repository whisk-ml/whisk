"""Main module."""
import whisk
from whisk.cli.log_tree import PARENT_TREE_NODE_PREFIX, CHILD_TREE_NODE_PREFIX
from cookiecutter.main import cookiecutter
from os.path import realpath
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


def to_slug(str):
    """
    Converts a string to a slug:

    * Makes all letters lowercase
    * Replaces spaces with underscores
    """
    return str.lower().replace(' ', '_')


def create(dir, force=False,
           module_name=None,
           dependency=f"whisk=={whisk.__version__}",
           install_requires=f"whisk=={whisk.__version__}"):
    """
    Creates a whisk project.

    Parameters
    ----------
    dir : str
        Path of the directory to create the project. The directory name is
        converted to a slug via :func:`project_name_to_slug`.

    module_name : str, optional
        Name of the module used when importing the project. This is converted to a
        slug via :func:`project_name_to_slug`. Default is the ``project_name``.

    force : bool, optional
        Recreates the project directory if it exists. Default is `False`.

    dependency : str, optional
        The whisk dependency entry in the project's requirements.txt file.
        Default locks to the current version. The version lock is restrictive
        as earlier and later versions of whisk could expect a different
        template structure and break functionality.

    install_requires : str, optional
        The whisk ``install_requires`` entry in the project's ``setup.py``
        file. Default locks to the current version. The version lock is
        restrictive as earlier and later versions of whisk could expect a
        different template structure and break functionality.
    """

    path = Path(dir).absolute()
    logger.debug(f"Creating project in {path}.")
    project_name = path.stem
    output_dir = path.parent

    project_name_slug = to_slug(project_name)
    if module_name:
        module_name_slug = to_slug(module_name)
    else:
        module_name_slug = project_name_slug

    # `whisk_dependency` is more flexible (for example, specifying a local
    # install) than `whisk_install_requires` and is used in testing to require
    # the local version of whisk.
    extra_content = {
        "repo_name": project_name_slug,
        "project_name": module_name_slug,
        "whisk_dependency": dependency,
        "whisk_install_requires": install_requires
    }
    logger.debug(f"Creating whisk project with extra_content={extra_content}")
    logger.info(PARENT_TREE_NODE_PREFIX +
                "Creating project directory structure...")
    res = cookiecutter(cookiecutter_template_dir(),
                       no_input=True,
                       overwrite_if_exists=force,
                       output_dir=output_dir,
                       extra_context=extra_content)
    logger.info(CHILD_TREE_NODE_PREFIX+"Project created in %s", res)
    logger.info(CHILD_TREE_NODE_PREFIX+"DONE.")
    return res
