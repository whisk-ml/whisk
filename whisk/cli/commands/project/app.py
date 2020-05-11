import click
from subprocess import call
import whisk.git as git

@click.group()
def cli():
    pass

@cli.command()
def start():
    """Start the HTTP web service."""
    call("honcho -f app/Procfile.dev start", shell=True)

@cli.command()
def create(name):
    """
    Create a Heroku app for the web service.
    """

@cli.command()
@click.argument("name")
def create(name):
    """
    Create a Heroku app for the web service with the given NAME.
    """
    if git.has_unstaged_changes():
        click.echo("This project has uncommitted changes.\n\nPlease add and commit the files to the Git repo, then retry:\n\ngit add .\ngit commit -m 'First Commit'\n")
        exit(1)
    call("heroku create -a {}".format(name), shell=True)
    call("heroku buildpacks:add -a {} https://github.com/heroku/heroku-buildpack-multi-procfile".format(name), shell=True)
    call("heroku buildpacks:add heroku/python", shell=True)
    call("heroku config:set PROCFILE=app/Procfile", shell=True)
    call("git push heroku master", shell=True)

@cli.command()
def destroy():
    """
    Delete the Heroku app.
    """
    call("heroku apps:destroy", shell=True)
