import click
from whisk import whisk
from whisk.cli.commands.project.setup import cli as setup_cli
import logging

logger = logging.getLogger(__name__)

@click.command()
@click.argument('name')
@click.option('--setup/--no-setup', default=True, help="Run setup script after creating directory structure.")
@click.option('--force/--no-force', default=False, help="Overwrite the contents of output directory if it exists.")
@click.option('-o', '--output_dir', default=".", help="The parent directory that will contain the project.")
@click.pass_context
def cli(ctx, name, setup, output_dir, force):
    """
    Creates a Whisk project in the NAME directory.

    When --setup is true (the default), `whisk setup` is run after the project structure has been created
    to setup the environment.
    """
    res = whisk.create(name, output_dir=output_dir, force=force)
    if setup:
        ctx.invoke(setup_cli, dir = res)
    else:
        logger.info("Skipping setup. Run later with `whisk setup`.")
    return res
