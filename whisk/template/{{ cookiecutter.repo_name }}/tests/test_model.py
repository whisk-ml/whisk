#!/usr/bin/env python
import pytest
import shutil
import os

# https://click.palletsprojects.com/en/7.x/testing/
from click.testing import CliRunner

from {{cookiecutter.project_name}}.models.model import Model
# TODO
#from {{cookiecutter.project_name}}.cli import cli
# from whisk.cli import cli
from pathlib import Path

def test_cli():
    """Test the CLI."""
    pass

    # runner = CliRunner()
    # result = runner.invoke(cli.main)
    # assert result.exit_code == 0
    # help_result = runner.invoke(cli.main, ['--help'])
    # assert help_result.exit_code == 0

def test_predict_via_cli():
    """Test creating an app via the CLI."""
    pass

    # project_name = "project_name_cli"
    # runner = CliRunner()
    # with runner.isolated_filesystem():
    #     result = runner.invoke(cli.create,[project_name, '--no-setup'])
    #     assert result.exit_code == 0
    #     assert os.path.exists((Path(os.getcwd()) / project_name))

def test_predict():
    model = Model()
    model.predict([[1,2],[3,4]])
