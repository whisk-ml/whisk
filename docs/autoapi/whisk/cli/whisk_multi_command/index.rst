:mod:`whisk.cli.whisk_multi_command`
====================================

.. py:module:: whisk.cli.whisk_multi_command


Module Contents
---------------


.. py:class:: WhiskMultiCommand(name=None, invoke_without_command=False, no_args_is_help=None, subcommand_metavar=None, chain=False, result_callback=None, **attrs)

   Bases: :class:`click.MultiCommand`

   This is a custom class based on https://github.com/pallets/click/blob/master/examples/complex/complex/cli.py
   that loads click command files at run time from both the whisk module commands and commands
   specified within the created project. This lets users override existing whisk cli commands and create new commands.

   Project-specific commands are only loaded if the the cwd is the project root.

   .. method:: core_commands_dir(self)

      Commands available whether in or outside a project.


   .. method:: core_project_commands_dir(self)

      whisk-provided project-only commands directory.


   .. method:: project_commands_dir(self)

      Custom project commands directory.


   .. method:: list_commands(self, ctx)

      MultiCommand classes must implement this function.
      This returns a set of file names across all directories.


   .. method:: _command_file_names(self, dir_name)

      Returns a list of file names minus the *.py file extension.
      This assumes that click commands are listed in directories containing only click command files.


   .. method:: _eval_file(self, fn)

      Evals the given filename, return the 'cli' namespace.
      The file must contain a 'cli' click command or group.

      If the file doesn't exist, nothing is returned.


   .. method:: get_command(self, ctx, name)

      MultiCommand classes must implement this function.

      Returns the CLI command w/the given name. The following load order is used:
      * Project-specific commands
      * Core commands
      * Core project-specific commands

      If a command is found it is returned immediately. For example, if both a custom project-specific
      command and a core project-specific command exist with the same name the custom command is returned,
      overriding the default.



