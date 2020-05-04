from invoke import Collection, task
import core.tasks

# Core Tasks
ns = Collection.from_module(core.tasks)

### Add project-specific tasks below. ###
# See http://docs.pyinvoke.org/en/stable/getting-started.html

from src.models.model_wrapper import ModelWrapper

@task(help={'data': "A single record to perform model inference"})
def predict(c, data):
    """
    Invokes the model.
    """
    model = ModelWrapper()
    print(model.predict([data]))

model = Collection('model')
model.add_task(predict)
ns.add_collection(model)
