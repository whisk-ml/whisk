:mod:`whisk.project`
====================

.. py:module:: whisk.project


Module Contents
---------------


.. py:class:: Project(dir=os.getcwd(), module_dir=None)

   Abstracts project-level attributes into a class.

   .. attribute:: dir
      

      The top-level project directory (str)


   .. attribute:: path
      

      The top-level project directory as a pathlib.Path


   .. attribute:: name
      

      Name of the project derived from the top-level directory (str)


   .. attribute:: module_dir
      

      Location of the project's module directory as a pathlib.Path.
      This is derived from `path` if not provided.


   .. attribute:: artifacts_dir
      

      Location of the project's artifacts directory as a pathlib.Path.
      This is derived from `path` if not provided.


   .. classmethod:: from_module(cls, path)

      Takes a path from a generated project's src/{{name}}/__init__.py file
      and returns a Project object Initialized w/that path.


   .. method:: validate_in_project(self)

      Raises an `OSError` if this is not a whisk project.


   .. method:: in_project(self)

      Returns True if the project's path is the root whisk
      project directory.

      This is deteremined by the presence of the ".whisk/" directory.



