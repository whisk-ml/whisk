from invoke import Collection, task

# Default tasks are in core.tasks
import {{cookiecutter.project_name}}.core.tasks.app as app
import {{cookiecutter.project_name}}.core.tasks.notebooks as notebooks
import {{cookiecutter.project_name}}.core.tasks.setup as setup
import {{cookiecutter.project_name}}.core.tasks.destroy as destroy



# Add default task collections
ns = Collection()
ns.add_collection(app)
ns = Collection(app)
ns.add_collection(notebooks)
ns.add_collection(setup)
ns.add_collection(destroy)
