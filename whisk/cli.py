"""Console script for whisk."""
import sys
import click
from whisk import whisk

@click.group()
def main():
    pass

@main.command()
@click.argument('name')
@click.option('--setup/--no-setup', default=True, help="Run setup script after creating directory structure.")
def create(name, setup):
    """Creates a Whisk project in the NAME directory."""
    whisk.create(name, setup=setup)

if __name__ == "__main__":
    main()
