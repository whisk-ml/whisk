import click
from whisk import whisk

@click.command()
@click.argument('name')
@click.option('--setup/--no-setup', default=True, help="Run setup script after creating directory structure.")
@click.option('--force/--no-force', default=False, help="Overwrite the contents of output directory if it exists.")
@click.option('-o', '--output_dir', default=".", help="The parent directory that will contain the project.")
def cli(name, setup, output_dir, force):
    """Creates a Whisk project in the NAME directory."""
    whisk.create(name, setup=setup, output_dir=output_dir, force=force)
