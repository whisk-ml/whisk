import click
from whisk import whisk
from whisk.project import Project
import os


class WhiskMultiCommand(click.MultiCommand):
    """
    This is a custom class based on
    https://github.com/pallets/click/blob/master/examples/complex/complex/cli.py
    that loads click command files at run time from both the whisk module
    commands and commands specified within the created project. This lets users
    override existing whisk cli commands and create new commands.

    Project-specific commands are only loaded if the the cwd
    is the project root.
    """

    def core_commands_dir(self):
        """Commands available whether in or outside a project."""
        return whisk.root_module_dir() / "cli/commands"

    def core_project_commands_dir(self):
        """whisk-provided project-only commands directory."""
        return self.core_commands_dir() / "project"

    def project_commands_dir(self):
        """Custom project commands directory."""
        return Project().commands_dir

    def list_commands(self, ctx):
        """
        MultiCommand classes must implement this function.
        This returns a set of file names across all directories.
        """
        project = Project()
        rv = []
        rv = rv + self._command_file_names(self.core_commands_dir())
        if project.in_project():
            rv = rv + self._command_file_names(
                                               self.core_project_commands_dir()
                                              )
            # Possible commands directory is deleted in project
            if project.commands_dir.exists():
                rv = rv + self._command_file_names(project.commands_dir)

        rv.sort()
        return set(rv)

    def _command_file_names(self, dir_name):
        """
        Returns a list of file names minus the *.py file extension.
        This assumes that click commands are listed in directories
        containing only click command files.
        """
        rv = []
        for filename in os.listdir(dir_name):
            if filename != '__init__.py' and filename.endswith(".py"):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def _eval_file(self, fn):
        """
        Evals the given filename, return the 'cli' namespace.
        The file must contain a 'cli' click command or group.

        If the file doesn't exist, nothing is returned.
        """
        if not os.path.isfile(fn):
            return

        ns = {}
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)

        if 'cli' in ns:
            return ns['cli']
        else:
            # The code was eval'd but did not have a `cli`
            # key in the namespace.
            return

    def get_command(self, ctx, name):
        """
        MultiCommand classes must implement this function.

        Returns the CLI command w/the given name. The following load order
        is used:
        * Project-specific commands
        * Core commands
        * Core project-specific commands

        If a command is found it is returned immediately. For example, if
        both a custom project-specific command and a core project-specific
        command exist with the same name the custom command is returned,
        overriding the default.
        """
        project = Project()

        if project.in_project():
            fn = os.path.join(self.project_commands_dir(), name + '.py')
            ns = self._eval_file(fn)

            if ns:
                return ns

        fn = os.path.join(self.core_commands_dir(), name + '.py')
        ns = self._eval_file(fn)

        if ns:
            return ns

        fn = os.path.join(self.core_project_commands_dir(), name + '.py')
        ns = self._eval_file(fn)
        return ns
