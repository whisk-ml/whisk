"""Main module."""

from cookiecutter.main import cookiecutter
from os.path import dirname, realpath
from pathlib import Path

def root_module_dir():
    """
    Returns a Path object with the root whisk module directory.
    """
    filepath = realpath(__file__)
    return Path(filepath).parents[0]

def cookiecutter_template_dir():
    return str(root_module_dir() / 'template/')

def create(project_name, output_dir=".", setup=None):
    """
    Creates a whisk project.
    """
    extra_content = {"project_name": project_name}
    if setup is not None:
        extra_content["setup"] = setup
    cookiecutter(cookiecutter_template_dir(),
                no_input=True,
                output_dir=output_dir,
                extra_context=extra_content)
