import click
from subprocess import call, check_output
from whisk.project import Project

project = Project()

@click.group()
def cli():
    pass

@cli.command()
def dist():
    """Builds a source distribution of the project."""
    call("python setup.py sdist > /dev/null", shell=True)
    click.echo("Python Package created in {}:".format(project.path / "dist"))
    res = check_output("ls -h dist", shell=True)
    click.echo(res)
