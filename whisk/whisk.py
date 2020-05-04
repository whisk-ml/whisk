"""Main module."""

from cookiecutter.main import cookiecutter

def create(project_name, output_dir=".", setup=None):
    print("creating=",project_name)
    extra_content = {"project_name": project_name}
    if setup is not None:
        extra_content["setup"] = setup
    print("extra_content",extra_content)
    cookiecutter('/Users/dlite/projects/whisk/whisk/template/',
                no_input=True,
                output_dir=output_dir,
                extra_context=extra_content)
