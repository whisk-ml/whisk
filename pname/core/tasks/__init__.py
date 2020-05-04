from invoke import Collection, task

# Default tasks are in core.tasks
import core.tasks.app as app
import core.tasks.notebooks as notebooks
import core.tasks.setup as setup
import core.tasks.destroy as destroy



# Add default task collections
ns = Collection()
ns.add_collection(app)
ns = Collection(app)
ns.add_collection(notebooks)
ns.add_collection(setup)
ns.add_collection(destroy)
