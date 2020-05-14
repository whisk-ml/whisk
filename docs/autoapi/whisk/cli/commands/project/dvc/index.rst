:mod:`whisk.cli.commands.project.dvc`
=====================================

.. py:module:: whisk.cli.commands.project.dvc


Module Contents
---------------


.. data:: project
   

   

.. function:: cli()


.. function:: remote_add(bucket)

   Adds a DVC S3 remote as the default remote using the provided S3 bucket.


.. function:: remote_remove(name)

   Removes the DVC S3 remote.


.. function:: setup()

   Initializes dvc, adds a local remote, and installs git post-checkout hooks.

   Run `dvc destroy` to revert.


