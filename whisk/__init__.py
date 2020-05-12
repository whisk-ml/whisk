"""Top-level package for whisk."""

__author__ = """Derek Haynes"""
__email__ = 'derek@dlite.cc'
__version__ = '0.1.22'

"""
Reference to the current whisk.Project. Set when whisk is loaded from
within a created project.
"""
project = None

"""
The location of the data directory. This is set from the Project instance and made
available as a top-level attribute since it is frequently used.
"""
data_dir = None
"""
The location of the artifacts directory. This is set from the Project instance and made
available as a top-level attribute since it is frequently used.
"""
artifacts_dir = None
