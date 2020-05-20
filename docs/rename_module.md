# Renaming the module

Follow the following steps if you wish to change the module name inside a whisk project. The module name is used when importing and when packaging the model:

```py
from <module name>.models.model import Model
model = Model()
model.predict(<input>)
```

If you'd like to change the directory name associated with the project, see the [Renaming the project directory](rename_project.html) guide.

## 1. Update setup.py

In the project's `setup.py` file, update the `setup` function's `name` argument and the cli command:

```diff
-    name='<old module name>',
+    name='<new module name>',
      entry_points={
        'console_scripts': [
-            '<old module name>=<old module name>.cli.main:cli',
+            '<new module name>=<new module name>.cli.main:cli',
        ],
    },
```

## 2. Update the src/<module name> directory

Rename the `src/<module name>` directory:

    mv src/<old module name> src/<new module name>

## 3. Find and replace the project name in project files

In your project files, find and replace `<old module name>.` with `<new module name>.`

## 4. Re-install the package

Type the following to re-install the package in editable mode:

    pip install -e .

## 5. Run tests

Run both `pytest` and `tox` to ensure all tests pass with the new project name.

## Extra considerations

### DVC

If your project is using [DVC](dvc.html), you may need to run [`dvc move`](https://dvc.org/doc/command-reference/move) to update the paths of files tracked with DVC.
