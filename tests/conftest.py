import os
import sys
import pytest
import shutil
from pathlib import Path
from cookiecutter import main
import whisk
from whisk.whisk import create
import whisk.setup

args = {
        'project_name': 'project_name',
        'author_name': 'DrivenData',
        'open_source_license': 'BSD-3-Clause',
        'python_interpreter': 'python3',
        'setup': True,
        }


def system_check(basename):
    platform = sys.platform
    if 'linux' in platform:
        basename = basename.lower()
    return basename


# Look into https://docs.pytest.org/en/latest/example/simple.html#request-example
# for handling command line options like skipping setup.
@pytest.fixture(scope='class', params=[{}, args])
def default_baked_project(tmpdir_factory, request):
    temp = tmpdir_factory.mktemp('data-project')
    out_dir = Path(temp).resolve()

    pytest.param = request.param
    # TODO - handle via a command-line option
    setup = True

    pytest.param = {
        "whisk_dependency": "-e {}".format(os.getcwd()),
        "setup": setup
    }

    project_name = pytest.param.get('project_name') or 'project_name'
    proj_dir = create(out_dir / project_name)
    proj = Path(proj_dir)
    if setup:
        whisk.setup.setup(proj)

    request.cls.path = proj
    yield

    # cleanup after
    shutil.rmtree(out_dir)
    # jupyter kernelspec list
    os.system("jupyter kernelspec uninstall {} -f".format(project_name))
