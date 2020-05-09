from setuptools import find_packages, setup

setup(
    name='{{cookiecutter.project_name}}',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    version='0.1.0',
    include_package_data=True,
    # By default only whisk is added as a dependency. whisk is required for
    # accessing whisk.project.artifacts_dir in the default models.model.Model class.
    # You likely need to list more dependencies for your model package.
    # For example: your model framework (Scikit, Torch, etc), numpy, Pandas, etc.
    #
    # Copying the requirements.txt dependencies into `install_requires=` isn't recommended as this
    # includes many dependencies that are not required to generate predictions and can result in a very large package.
    #
    # You can test that the package works and contains needed dependencies by running `tox` from the
    # command line. tox tests the package in an isoloated venv.
    install_requires=[
        '{{cookiecutter.whisk_install_requires}}'
    ],
    entry_points={
        'console_scripts': [
            '{{cookiecutter.project_name}}={{cookiecutter.project_name}}.cli.main:cli',
        ],
    },
    description='A short description of the project.',
    author='Your name (or your organization/company/team)',
    author_email='you@example.com',
    python_requires='>=3.6',
    url="https://ADD THE URL TO YOUR PROJECT GITHUB REPO OR DOCS"
)
