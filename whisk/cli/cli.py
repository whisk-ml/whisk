"""
Console script for whisk.
Structure is based on https://github.com/pallets/click/blob/master/examples/complex.
"""
import sys
import click
from whisk import whisk
from whisk.project import Project
from whisk.cli.whisk_multi_command import WhiskMultiCommand

@click.command(cls=WhiskMultiCommand)
def cli():
    pass

if __name__ == "__main__":
    cli()
