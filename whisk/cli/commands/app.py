import click

@click.group()
def app():
    pass

@app.command()
def start():
    """Start the HTTP web service."""
    print("starting")

@app.command()
def create(name):
    """
    Create a Heroku app for the web service.
    """
