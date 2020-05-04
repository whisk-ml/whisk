from invoke import task
import sys
import subprocess

@task
def start(c):
    """
    Start the web service serving model inference.
    """
    c.run("honcho -f app/Procfile.dev start", pty=True)

def has_unstaged_changes():
    res=subprocess.check_output("git status --porcelain",shell=True, universal_newlines=True)
    return ("\n" in res)

@task(help={'name': "Name of the Heroku app."})
def create(c,name):
    """
    Create a Heroku app for the web service.
    """
    if has_unstaged_changes():
        print("This project has uncommitted changes.\nPlease add and commit the files to the Git repo, then retry:\n\ngit add .\ngit commit -m 'First Commit'")
        exit(1)
    c.run("heroku create -a {}".format(name))
    c.run("heroku buildpacks:add -a {} https://github.com/heroku/heroku-buildpack-multi-procfile".format(name))
    c.run("heroku buildpacks:add heroku/python")
    c.run("heroku config:set PROCFILE=app/Procfile")
    c.run("git push heroku master")

@task
def destroy(c):
    """
    Delete the Heroku app.
    """
    c.run("heroku apps:destroy", pty=True)

@task
def test(c):
    """
    Run the web service unit tests.
    """
    c.run("python app/test.py")
