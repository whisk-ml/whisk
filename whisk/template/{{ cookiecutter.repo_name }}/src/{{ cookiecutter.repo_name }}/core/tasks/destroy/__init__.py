from invoke import Collection
import {{cookiecutter.project_name}}.core.tasks.destroy.s3

ns = Collection()
ns.add_collection(s3)
