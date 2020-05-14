:mod:`whisk.cli.commands.project.setup`
=======================================

.. py:module:: whisk.cli.commands.project.setup


Module Contents
---------------


.. data:: NOTEBOOK_EXAMPLE_PATH
   :annotation: = notebooks/getting_started.ipynb

   

.. function:: has_unstaged_changes()


.. function:: exec(desc, cmd)

   Executes the `cmd`, and prints `desc` prior to execution.
   If the exit code is nonzero, raises a `SystemExit` execption.


.. function:: exec_setup(nbenv)


.. function:: set_example_notebook_kernel(nbenv)


.. function:: cli()

   Sets up the project environment.


