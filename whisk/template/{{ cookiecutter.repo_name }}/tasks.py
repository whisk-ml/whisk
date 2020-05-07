from invoke import Collection, task
import {{cookiecutter.project_name}}.core.tasks

# Core Tasks
ns = Collection.from_module({{cookiecutter.project_name}}.core.tasks)

### Add project-specific tasks below. ###
# See http://docs.pyinvoke.org/en/stable/getting-started.html

from {{cookiecutter.project_name}}.models.model import Model

@task(help={'data': "A single record to perform model inference"})
def predict(c, data):
    """
    Invokes the model.
    """
    model = Model()
    print(model.predict([data]))

model = Collection('model')
model.add_task(predict)
ns.add_collection(model)
