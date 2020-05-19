import click
import whisk.setup
import logging
import os

from subprocess import PIPE, STDOUT

logger = logging.getLogger(__name__)

@click.command()
@click.option('-d', '--dir', default=os.getcwd(), help="The project directory.", show_default=True)
def cli(dir):
    """
    Sets up the project environment.
    This is called by default after `whisk create` and should be run manually after cloning an existing project.

    See :func:`whisk.setup.setup` for the full list of steps that are performed.
    """
    whisk.setup.setup(dir)
