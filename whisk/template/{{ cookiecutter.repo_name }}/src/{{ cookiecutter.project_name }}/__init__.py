from os.path import realpath
import whisk
from whisk.project import Project


whisk.project = Project.from_module(realpath(__file__))


data_dir = whisk.project.data_dir
"""Location of the training data directory as a pathlib.Path."""


artifacts_dir = whisk.project.artifacts_dir
"""Location of the artifacts directory as a pathlib.Path."""
