import os
import sys
import pytest
import shutil
from pathlib import Path
from cookiecutter import main
import whisk
from whisk.whisk import cookiecutter_template_dir

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


@pytest.fixture(scope='class', params=[{}, args])
def default_baked_project(tmpdir_factory, request):
    temp = tmpdir_factory.mktemp('data-project')
    out_dir = Path(temp).resolve()

    pytest.param = request.param

    main.cookiecutter(
        cookiecutter_template_dir(),
        no_input=True,
        extra_context=pytest.param,
        output_dir=out_dir
    )

    pn = pytest.param.get('project_name') or 'project_name'

    # project name gets converted to lower case on Linux but not Mac
    pn = system_check(pn)

    proj = out_dir / pn
    request.cls.path = proj
    yield

    # cleanup after
    shutil.rmtree(out_dir)
    # jupyter kernelspec list
    os.system("jupyter kernelspec uninstall {} -f".format(pn))
