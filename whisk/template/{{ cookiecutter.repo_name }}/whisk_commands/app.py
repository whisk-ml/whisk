"""
Whisk includes default cli commands for performing common tasks in an ML project.
You can add new commands to your project and override existing commands. Files in this directory are
loaded as click commands.

This is an example of adding a new command (whisk app hello) and
overriding an existing command (whisk app start). Uncomment the code below to try it.

Click docs: https://click.palletsprojects.com/
For commands to load, the file must have a click `cli` command or group.
"""

import click
import subprocess

# @click.group()
# def cli():
#     pass
#
# @cli.command()
# def hello():
#     """Hello!"""
#     click.echo("Hello!")
#
# @cli.command()
# def start():
#     """Start override!!!!"""
#     click.echo("start override!!!!!!!!!!!!")
