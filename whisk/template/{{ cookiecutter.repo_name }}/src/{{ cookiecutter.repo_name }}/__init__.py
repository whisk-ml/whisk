from os.path import realpath
import whisk
from whisk.project import Project

"""
Initializes the whisk.project attribute so project helpers can be accessed via
whisk.project.*.
"""
whisk.project = Project.from_module(realpath(__file__))
whisk.data_dir = whisk.project.data_dir
whisk.artifacts_dir = whisk.project.artifacts_dir
