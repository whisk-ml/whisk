# Renaming the project directory

Follow the following steps if you wish to change the directory name of a whisk project.

If you'd like to change the module name used when calling `import`, running the CLI, or distributing the package, see the [Renaming the module](rename_module.html) guide.

## 1. Change the directory name

Update the name of the project directory:

    mv <old project name> <new project name>

## 2. Re-create the project virtual environment

The virtual environment contains hard-coded full paths that need to be updated with the new directory name. Run the following to re-create the virtual environment from within the project directory:

    python3 -m venv venv
    pip install -r requirements.txt
