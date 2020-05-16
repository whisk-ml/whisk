"""Manage the web service."""
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
@click.argument("name")
def create(name):
    """
    Create a Heroku app for the web service with the given NAME. The NAME must be unique across all Heroku apps.

    A Heroku deploy performs the following steps:

    * Ensures there are no unstaged commits before creating the app. If there are uncommited changes the command exists with a warning.\n
    * Creates the Heroku app\n
    * Adds the `Multi-Procfile buildpack <https://github.com/heroku/heroku-buildpack-multi-procfile />`_ to access the Procfile within the ``app/`` folder of the project.\n
    * Adds the `Python buildpack <https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-python />`_.\n
    * Sets a `PROCFILE` config var to ``app/Procfile``.\n
    * Pushes the git repo to Heroku.\n
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
