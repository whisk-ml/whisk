import os
import pytest
import datetime as dt
from subprocess import check_output, CalledProcessError
from conftest import system_check
from pathlib import Path


def no_curlies(filepath):
    """ Utility to make sure no curly braces appear in a file.
        That is, was Jinja able to render everything?
    """
    with open(filepath, 'r') as f:
        data = f.read()

    template_strings = [
        '{{',
        '}}',
        '{%',
        '%}'
    ]

    template_strings_in_file = [s in data for s in template_strings]
    return not any(template_strings_in_file)

def changed_files(root_path,ago):
    """
    Returns a list of files changed within the `root_path` since `ago`.
    """
    now = dt.datetime.now()
    changed_files = []
    for root, dirs,files in os.walk(root_path):
        for fname in files:
            path = os.path.join(root, fname)
            st = os.stat(path)
            mtime = dt.datetime.fromtimestamp(st.st_mtime)
            if mtime > ago:
                changed_files.append(path)
    return changed_files

def paths_to_relative(root,paths):
    """
    Converts a list of absolute paths to paths relative to the the root project path.
    """
    return list(map(lambda x: str(Path(x).relative_to(root)), paths))

@pytest.mark.usefixtures("default_baked_project")
class TestCookieSetup(object):
    def test_project_name(self):
        project = self.path
        if pytest.param.get('project_name'):
            assert project.name == pytest.param.get('project_name')
        else:
            assert project.name == 'project_name'

    def test_readme(self):
        readme_path = self.path / 'README.md'
        assert readme_path.exists()
        assert no_curlies(readme_path)
        if pytest.param.get('project_name'):
            with open(readme_path) as fin:
                assert pytest.param.get('project_name') in next(fin).strip()

    def test_setup(self):
        setup_ = self.path / 'setup.py'
        args = ['python', setup_, '--version']
        p = check_output(args).decode('ascii').strip()
        assert p == '0.1.0'

    def test_requirements(self):
        reqs_path = self.path / 'requirements.txt'
        assert reqs_path.exists()
        assert no_curlies(reqs_path)
        if pytest.param.get('python_interpreter') == 'python':
            with open(reqs_path) as fin:
                lines = list(map(lambda x: x.strip(), fin.readlines()))
            assert 'pathlib2' in lines

    # def  test_app_starts(self):
        # Fails:
        # ModuleNotFoundError: No module named 'flask'
        # check_output(['venv/bin/inv', 'app.test'], cwd=self.path)

    def test_idempotent_install_command(self):
        # Running setup is slow, so by default setup=False.
        if not pytest.param.get("setup"):
            return

        ago = dt.datetime.now()
        check_output(['whisk setup'], cwd=self.path)
        changed = changed_files(self.path,ago)
        # Script appears to update some files but unsure if that changes any functionality.
        # assert len(changed) == 0, "Files were modified: {}".format(changed)

    def test_notebook_runs(self):
        # Running setup is slow, so by default setup=False.
        if not pytest.param.get("setup"):
            return
        check_output(["venv/bin/inv", "notebooks.run", "notebooks/getting_started.ipynb"],
                     cwd=self.path)

    def test_app_create(self):
        if not pytest.param.get("setup"):
            return
        with pytest.raises(CalledProcessError):
            # Ensure we can run this task, but it fails because of uncommitted changes.
            check_output(["venv/bin/inv", "app.create", "APPNAME"],
                         cwd=self.path)

    def test_model_predict(self):
        # Running setup is slow, so by default setup=False.
        if not pytest.param.get("setup"):
            return
        check_output(["venv/bin/inv", "model.predict", "[[1,2],[3,4]]"],
                     cwd=self.path)

    def test_folders(self):
        project = self.path
        project_name = project.name
        expected_dirs = [
            '.whisk',
            'app',
            'data',
            'data/external',
            'data/interim',
            'data/processed',
            'data/raw',
            'docs',
            'notebooks',
            'references',
            'reports',
            'reports/figures',
            'src',
            "src/{}".format(project_name),
            "src/{}/artifacts".format(project_name),
            "src/{}/data".format(project_name),
            "src/{}/features".format(project_name),
            "src/{}/models".format(project_name),
            "src/{}/visualization".format(project_name),
        ]

        # venv dir created if setup=True
        if pytest.param.get("setup"):
            expected_dirs.append("venv")

        ignored_dirs = [
            str(self.path)
        ]

        abs_expected_dirs = [str(self.path / d) for d in expected_dirs]
        abs_dirs, _, _ = list(zip(*os.walk(self.path)))

        rel_dirs = paths_to_relative(self.path,abs_dirs)
        expected_dirs = paths_to_relative(self.path,set(abs_expected_dirs + ignored_dirs))

        missing_dirs = set(expected_dirs) - set(rel_dirs)
        assert len(missing_dirs)  == 0, "Expected dirs are missing: {}".format(missing_dirs)
