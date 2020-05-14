"""
Console script for whisk. The structure is based on `Click complex example app <https://github.com/pallets/click/blob/master/examples/complex/>`_.
"""
import sys
import click
from whisk import whisk
from whisk.project import Project
from whisk.cli.whisk_multi_command import WhiskMultiCommand

@click.command(cls=WhiskMultiCommand)
def cli():
    """Entry point for the whisk cli."""
    pass

if __name__ == "__main__":
    cli()
