# Renaming a project

Follow the following steps if you wish to change the name of a whisk project.

## 1. Update setup.py

In the project's `setup.py` file, update the `setup` function's `name` argument and the cli command:

```diff
-    name='<old project name>',
+    name='<new project name>',
      entry_points={
        'console_scripts': [
-            '<old project name>=<old project name>.cli.main:cli',
+            '<new project name>=<new project name>.cli.main:cli',
        ],
    },
```

## 2. Update the src/<project name> directory

Rename the `src/<project name>` directory:

    mv src/<old project name> src/<new project name>

## 3. Find and replace the project name in project files

In your project files, find and replace `<old project name>.` with `<new project name>.`

## 4. Re-install the package

Type the following to re-install the package in editable mode:

    pip install -e .

## 5. Run tests

Run both `pytest` and `tox` to ensure all tests pass with the new project name.

## Extra considerations

### DVC

If your project is using [DVC](dvc.html), you may need to run [`dvc move`](https://dvc.org/doc/command-reference/move) to update the paths of files tracked with DVC.
