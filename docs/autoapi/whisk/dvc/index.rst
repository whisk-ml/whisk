:mod:`whisk.dvc`
================

.. py:module:: whisk.dvc


Module Contents
---------------


.. function:: pull(dvc_file)

   Pulls the output of the specified `dvc_file` into the repository.
   This is useful when running outside the local environment (like a deployed web server)
   that doesn't have all data files by default.

   If `dvc pull` fails (has a non-zero exit status), a `subprocess.CalledProcessError` exception
   is raised.


