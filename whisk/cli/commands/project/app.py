import click
import subprocess

@click.group()
def cli():
    pass

@cli.command()
def start():
    """Start the HTTP web service."""
    subprocess.call("honcho -f app/Procfile.dev start", shell=True)

@cli.command()
def create(name):
    """
    Create a Heroku app for the web service.
    """
