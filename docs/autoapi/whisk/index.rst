:mod:`whisk`
============

.. py:module:: whisk

.. autoapi-nested-parse::

   Top-level package for whisk.



Subpackages
-----------
.. toctree::
   :titlesonly:
   :maxdepth: 3

   cli/index.rst


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   dvc/index.rst
   git/index.rst
   model_stub/index.rst
   project/index.rst
   whisk/index.rst


Package Contents
----------------

.. data:: __author__
   :annotation: = Derek Haynes

   

.. data:: __email__
   :annotation: = derek@dlite.cc

   

.. data:: __version__
   :annotation: = 0.1.24

   

.. data:: project
   

   Reference to the current :class:`whisk.project.Project`. Set when whisk is loaded from
   within a created project.


.. data:: data_dir
   

   The location of the data directory as a `pathlib.Path <https://docs.python.org/3.8/library/pathlib.html#basic-use/>`_. This is set from the Project instance and made
   available as a top-level attribute since it is frequently used.


.. data:: artifacts_dir
   

   The location of the artifacts directory as a `pathlib.Path <https://docs.python.org/3.8/library/pathlib.html#basic-use/>`_. This is set from the Project instance and made
   available as a top-level attribute since it is frequently used.


