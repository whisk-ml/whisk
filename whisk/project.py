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
        path_obj = Path(path)
        obj = cls(path_obj.parents[2],module_dir=path_obj.parents[0])
        return obj

    def __init__(self, dir=os.getcwd(), module_dir=None):
        """
        Initializes a project from the existing whisk project directory `dir`.
        """
        self.dir = dir
        self.path = Path(self.dir)
        self.module_dir = module_dir
        if not self.module_dir:
            self.module_dir = self.path / "src/{}".format(self.slug())
        self.artifacts_dir = self.module_dir / "artifacts"
        if self.in_project():
            self.data_dir = self.path/ "data"

    def validate_in_project(self):
        if not self.in_project():
            raise OSError("{} is not a whisk project directory.".format(self.dir))

    def in_project(self):
        """
        Returns True if the current working directory is root whisk
        project directory.
        """
        return (self.path / ".whisk").is_dir()

    def slug(self):
        """
        Returns the project slug derived from the project directory name.
        """
        return self.path.stem
