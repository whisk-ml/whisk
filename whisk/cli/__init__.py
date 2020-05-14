"""
This module contains whisk command line interface (CLI) commands and logic for managing whisk projects.

Commands within :mod:`whisk.cli.commands.project` are only loaded when the current working directory is the top-level of a whisk project.

:class:`whisk.cli.whisk_multi_command.WhiskMultiCommand` loads the commands based on the current working directory. If ran within a project, it also loads commands defined in the ``whisk_commands/`` directory.
"""
