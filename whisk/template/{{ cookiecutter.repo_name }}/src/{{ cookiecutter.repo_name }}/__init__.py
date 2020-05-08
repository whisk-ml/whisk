from os.path import realpath
from whisk.project import Project

project = Project.from_module(realpath(__file__))
