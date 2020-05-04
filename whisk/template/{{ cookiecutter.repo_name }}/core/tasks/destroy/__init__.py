from invoke import Collection
import core.tasks.destroy.s3

ns = Collection()
ns.add_collection(s3)
