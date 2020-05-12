import os
# https://docs.python.org/3/library/pathlib.html
# Object-oriented filesystem paths
from pathlib import Path

class Project:
    """
    Abstracts project-level attributes into a class.
    """

    @classmethod
    def from_module(cls,path):
        """
        Takes a path from a generated project's src/{{name}}/__init__.py file
        and returns a Project object Initialized w/that path.
        """
        path_obj = Path(path)
        obj = cls(path_obj.parents[2],module_dir=path_obj.parents[0])
        return obj

    def __init__(self, dir=os.getcwd(), module_dir=None):
        """
        Initializes a project from the existing whisk project directory `dir`.
        """
        self.dir = dir
        """The top-level project directory (str)"""
        self.path = Path(self.dir)
        """The top-level project directory as a pathlib.Path"""
        self.name = self.path.stem
        """Name of the project derived from the top-level directory (str)"""
        self.module_dir = module_dir
        """
        Location of the project's module directory as a pathlib.Path.
        This is derived from `path` if not provided.
        """
        if not self.module_dir:
            self.module_dir = self.path / "src/{}".format(self.name)
        self.artifacts_dir = self.module_dir / "artifacts"
        """
        Location of the project's artifacts directory as a pathlib.Path.
        This is derived from `path` if not provided.
        """
        if self.in_project():
            self.data_dir = self.path / "data"
            """
            Location of the project's data directory as a pathlib.Path.
            This is only set if with a valid whisk project.
            """
            self.commands_dir = self.path / "whisk_commands"
            """
            Location of the project's whisk commands directory as a pathlib.Path.
            This is only set if with a valid whisk project.
            """

    def validate_in_project(self):
        """
        Raises an `OSError` if this is not a whisk project.
        """
        if not self.in_project():
            raise OSError("{} is not a whisk project directory.".format(self.dir))

    def in_project(self):
        """
        Returns True if the project's path is the root whisk
        project directory.

        This is deteremined by the presence of the ".whisk/" directory.
        """
        return (self.path / ".whisk").is_dir()
