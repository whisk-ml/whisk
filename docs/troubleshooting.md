# Troubleshooting

### Errors running `whisk create` or `whisk setup`

If you encounter errors running `whisk create` or `whisk setup` please follow the following steps:

1. Re-run the command with the `--log-file` global option. This logs critical debugging information to a file. For example:
    ```
    $ whisk --log-file whisk.log create <project_name>
    ```
2. Create a [GitHub issue](https://github.com/whisk-ml/whisk/issues/new) describing your problem. Provide the log file output in the issue.

### Other errors

Create a [GitHub issue](https://github.com/whisk-ml/whisk/issues/new) describing your problem. Please provide the following information about your computing environment in the issue:

* whisk version (`pip show whisk`)
* Operating system and version
* Python version (`python --version`)
