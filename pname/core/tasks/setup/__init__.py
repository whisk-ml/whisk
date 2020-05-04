from invoke import Collection
import core.tasks.setup.s3

ns = Collection()
ns.add_collection(s3)
