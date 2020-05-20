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
@click.option('--module-name', help="The name of the module to use when calling `import` and when packaging.")
@click.option('--dependency', help="The whisk dependency entry in the project's requirements.txt file.")
@click.option('--install-requires', help="The whisk `install_requires entry in the project's `setup.py` file")

@click.pass_context
def cli(ctx, name, setup, output_dir, force, module_name, dependency, install_requires):
    """
    Creates a Whisk project in the NAME directory.

    When --setup is true (the default), `whisk setup` is run after the project structure has been created
    to setup the environment.
    """

    kwargs = {}
    if output_dir:
        kwargs["output_dir"] = output_dir
    if force:
        kwargs["force"] = force
    if module_name:
        kwargs["module_name"] = module_name
    if dependency:
        kwargs["dependency"] = dependency
    if install_requires:
        kwargs["install_requires"] = install_requires

    res = whisk.create(name, **kwargs)
    if setup:
        ctx.invoke(setup_cli, dir = res)
    else:
        logger.info("Skipping setup. Run later with `whisk setup`.")
    return res
