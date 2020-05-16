# CLI Reference

The whisk command line is used to manage your whisk project. Use the `whisk` command to create a new project, start the web service, setup a project you've cloned via git, and more.

To obtain a list of commands and command groups, type `whisk --help`. You'll see output like below:

    $ whisk --help
    Usage: whisk [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      create    Creates a Whisk project in the NAME directory.
      setup     Sets up the project environment.
      app
      package
      notebook
      s3
      dvc

Commands that don't have a description are groups that have additional sub commands. To view commands within a group, type `whisk [GROUP] --help`. For example:

    $ whisk app --help
    Usage: whisk app [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      create   Create a Heroku app for the web service with the given NAME.
      destroy  Delete the Heroku app.
      start    Start the HTTP web service.

To get help on a specific command, append `--help` to the command. For example:

    $ whisk create --help
    Usage: whisk create [OPTIONS] NAME

      Creates a Whisk project in the NAME directory.

    Options:
      --setup / --no-setup   Run setup script after creating directory structure.
      --force / --no-force   Overwrite the contents of output directory if it
                             exists.

      -o, --output_dir TEXT  The parent directory that will contain the project.
      --help                 Show this message and exit.

### whisk create

Create a new project by running `whisk create [PROJECT_NAME]` after [installing whisk](installation.html).

`whisk create` sets up the [directory structure](project_structure.html), and initializes the project environment ([see the setup API docs](autoapi/whisk/cli/commands/project/setup/index.html#whisk.cli.commands.project.setup.cli) for list of operations). This gives you everything needed to get started on your ML project.

### whisk setup

If you've cloned an existing whisk project, run `whisk setup` within the project to create a venv and install dependencies. See the [API docs on setup](autoapi/whisk/cli/commands/project/setup/index.html#whisk.cli.commands.project.setup.cli) for a full list of operations this command performs.

### whisk app start

Starts the Flask web service. The code for the Flask app is in the `app/` directory of the project.

### whisk app create

Deploys the Flask web service to Heroku. Requires a `name` command argument:

    $ whisk app create [NAME OF THE HEROKU APP]

The name must be unique on Heroku. See the [API docs](autoapi/whisk/cli/commands/project/app/index.html#whisk.cli.commands.project.app.create) for details on the steps performed to create an app on Heroku.

### whisk app destroy

Destroys the Heroku app.

### whisk s3 create

Creates an S3 bucket to store data. If no bucket name is provided, the bucket name is generated from the project directory name.

### whisk s3 delete

Deletes the existing S3 bucket used to store data. If no bucket name is provided, the bucket name is generated from the project directory name.

### whisk s3 make-public

Creates a public read-only policy for the S3 bucket. This grants anonymous users read-only access to objects within the bucket.

### whisk s3 delete-policy

Deletes the policy associated with the S3 bucket.

### whisk dvc remote-add

Adds a DVC S3 remote as the default remote using the provided S3 bucket. Run [`whisk s3 create`](#whisk-s3-create) prior to adding the remote.

### whisk dvc remote-remove

Removes the DVC S3 remote.

### whisk dvc setup

Initializes dvc, adds a local remote, and installs git post-checkout hooks. Run `dvc destroy` to revert.

### whisk notebook run

Run a notebook from the command line with the given `RELATIVE_PATH`. Example:

    $ whisk notebook run notebooks/getting_started.ipynb

### whisk package dist

Builds a source distribution of the project. Example:

    $ whisk package dist
    Python Package created in /Users/dlite/projects/whisk_examples/demo/dist:
    demo-0.1.0.tar.gz

To install:

    $ pip install dist/demo-0.1.0.tar.gz

See the [packaging](packaging.html) guide for more information on packaging your code.
