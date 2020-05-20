import click
from whisk import whisk
from whisk.cli.commands.project.setup import cli as setup_cli
import logging
import cookiecutter

logger = logging.getLogger(__name__)

@click.command()
@click.argument('project-path')
@click.option('--setup/--no-setup', default=True, show_default=True, help="Run `whisk setup` to configure the project environment.")
@click.option('--force/--no-force', default=False, show_default=True, help="Overwrite the contents of output directory if it exists.")
@click.option('--module-name', help="The name of the module to use when calling `import` and when packaging.")
@click.option('--dependency', help="The whisk dependency entry in the project's requirements.txt file.")
@click.option('--install-requires', help="The whisk `install_requires` entry in the project's `setup.py` file")

@click.pass_context
def cli(ctx, project_path, setup, force, module_name, dependency, install_requires):
    """
    Creates a new whisk project with a default directory structure and
    environment at the path you specify.
    """

    kwargs = {}
    if force:
        kwargs["force"] = force
    if module_name:
        kwargs["module_name"] = module_name
    if dependency:
        kwargs["dependency"] = dependency
    if install_requires:
        kwargs["install_requires"] = install_requires

    try:
        res = whisk.create(project_path, **kwargs)
    except cookiecutter.exceptions.OutputDirExistsException:
        logger.error(
f"""
Aborting project creation - the directory {project_path} already exist.
Re-run with `whisk create --force` to force creation.
"""
)
        exit(1)
    if setup:
        ctx.invoke(setup_cli, dir = res)
    else:
        logger.info("Skipping setup. Run later with `whisk setup`.")
    return res
