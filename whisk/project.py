import os
# https://docs.python.org/3/library/pathlib.html
# Object-oriented filesystem paths
from pathlib import Path

class Project:
    """
    Abstracts project-level attributes into a class.
    """

    def __init__(self,dir=os.getcwd()):
        """
        Initializes a project from the existing whisk project directory `dir`.

        If `dir` is not a whisk project an `OSError` is raised.
        """
        self.dir = dir
        self.path = Path(self.dir)
        self.validate_in_project()

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
