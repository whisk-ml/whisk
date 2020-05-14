:mod:`whisk.whisk`
==================

.. py:module:: whisk.whisk

.. autoapi-nested-parse::

   Main module.



Module Contents
---------------


.. function:: root_module_dir()

   Returns a Path object with the root whisk module directory.


.. function:: cookiecutter_template_dir()


.. function:: create(project_name, output_dir='.', setup=None, force=False)

   Creates a whisk project.

   Parameters
   ----------
   project_name : str
       Name of the directory to create for the project.

   output_dir : str, optional
       Path to create the directory. Default is the current working directory.

   setup : bool, optional
       Whether to run the post-creation setup command. By default this is `True`. If `False`, only the directory structure is created.

   force : bool, optional
       Recreates the project directory if it exists. Default is `False`.


