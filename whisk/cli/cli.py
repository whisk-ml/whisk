"""
Console script for whisk.
Groups structure is based on https://stackoverflow.com/a/39416589/1234395.
"""
import sys
import click
from whisk import whisk
from whisk.project import Project
from .commands.app import app
from .commands.setup import setup

def load_project_commands(click_group):
    """
    If inside a whisk project directory, project-specific commands are added to the cli.
    """
    if Project().in_project():
        click_group.add_command(app)
        click_group.add_command(setup)

@click.group()
def main():
    pass

@main.command()
@click.argument('name')
@click.option('--setup/--no-setup', default=True, help="Run setup script after creating directory structure.")
@click.option('--force/--no-force', default=False, help="Overwrite the contents of output directory if it exists.")
@click.option('-o', '--output_dir', default=".", help="The parent directory that will contain the project.")
def create(name, setup, output_dir, force):
    """Creates a Whisk project in the NAME directory."""
    whisk.create(name, setup=setup, output_dir=output_dir, force=force)

load_project_commands(main)

if __name__ == "__main__":
    main()
