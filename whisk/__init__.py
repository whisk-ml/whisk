"""Top-level package for whisk."""

__author__ = """Derek Haynes"""
__email__ = 'derek@dlite.cc'
__version__ = '0.1.31'

project = None
"""
Reference to the current :class:`whisk.project.Project`. Set when whisk is loaded from
within a created project.
"""

data_dir = None
"""
The location of the data directory as a `pathlib.Path <https://docs.python.org/3.8/library/pathlib.html#basic-use/>`_. This is set from the Project instance and made
available as a top-level attribute since it is frequently used.
"""

artifacts_dir = None
"""
The location of the artifacts directory as a `pathlib.Path <https://docs.python.org/3.8/library/pathlib.html#basic-use/>`_. This is set from the Project instance and made
available as a top-level attribute since it is frequently used.
"""
