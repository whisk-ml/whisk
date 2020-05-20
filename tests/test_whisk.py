#!/usr/bin/env python

"""Tests for `whisk` package."""

import pytest
import shutil
import os

# https://click.palletsprojects.com/en/7.x/testing/
from click.testing import CliRunner

from whisk import whisk
from whisk.cli import cli
from pathlib import Path

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_cli():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.cli)
    assert result.exit_code == 0
    help_result = runner.invoke(cli.cli, ['--help'])
    assert help_result.exit_code == 0

def test_create_via_cli():
    """Test creating an app via the CLI."""
    project_name = "project_name_cli"
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli.cli,['create', project_name, '--no-setup'])
        assert result.exit_code == 0
        assert os.path.exists((Path(os.getcwd()) / project_name))

def test_create(tmpdir):
    temp = tmpdir.mkdir('whisk-project')
    project_name = "project_name"
    out_dir = Path(temp).resolve()
    whisk.create(out_dir / project_name)
    shutil.rmtree(out_dir)
