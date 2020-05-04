#!/usr/bin/env python

"""Tests for `whisk` package."""

import pytest
import shutil

from click.testing import CliRunner

from whisk import whisk
from whisk import cli
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


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'whisk.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

def test_create(tmpdir):
    temp = tmpdir.mkdir('data-project')
    project_name = "project_name"
    out_dir = Path(temp).resolve()
    whisk.create(project_name, output_dir=out_dir, setup=False)
    shutil.rmtree(out_dir)
