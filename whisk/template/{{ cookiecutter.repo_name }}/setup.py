from setuptools import find_packages, setup

def list_reqs(fname='requirements.txt'):
    """
    Adds the packages listed in `fname` as package requirements.

    By default this is the project's main requirements.txt file. To provide
    a smaller set of packages required only for model predictions, add a
    `src/requirements.txt` file w/the subset of required packages and load this file instead.
    """
    with open(fname) as fd:
        return fd.read().splitlines()

setup(
    name='{{cookiecutter.project_name}}',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    version='0.1.0',
    include_package_data=True,
    # TODO - show how to include dependencies with install_requires
    # install_requires=list_reqs(),
    entry_points={
        'console_scripts': [
            '{{cookiecutter.project_name}}={{cookiecutter.project_name}}.cli.main:cli',
        ],
    },
    description='A short description of the project.',
    author='Your name (or your organization/company/team)',
    python_requires='>=3.6',
)
