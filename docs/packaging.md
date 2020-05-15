# Packaging

The whisk project structure is a machine learning-flavor of a typical Python project. This baked-in structure means you can easily [package your work and distribute](https://packaging.python.org/guides/distributing-packages-using-setuptools/) a trained model as a standard Python Package. End users can then install the package with `pip install`. __As pip is part of the Python standard library, any user with Python installed on their computer now has access to your model.__

## How it works

A whisk project includes the following to generate a Python package of your trained model:

* `setup.py` - This is the [most important file](https://packaging.python.org/guides/distributing-packages-using-setuptools/#setup-py) for packaging and exists in the root of the project. It specifies your package dependencies and metadata (like the name of the package, author, description, etc.).
* `MANIFEST.in` - Needed to package files that are not automatically included in the source distribution.
* `src/<project_name>` - Only files within this directory are included in the package. The package will be named `<project_name>` and can be imported via `import <project_name>`.

## Packaging steps

The following flow is suggested when packaging your work for distribution:

### 1. Test your package with tox

A whisk project comes with [tox](https://tox.readthedocs.io/en/latest/). With tox, we can build the source distribution, install it in its own isolated environment, and test it against multiple Python versions. By installing the package in an isolated environment we can ensure it includes all needed dependencies and stands on its own.

Type the following in the project root directory to run tox:

    $ tox

It's common for the tests to initially fail for two reasons:

### Missing dependencies

The project's `setup.py` only includes `whisk` as a default dependency. The dependencies listed in your project's `requirements.txt` are not referenced from `setup.py` as `requirements.txt` likely includes many packages that aren't needed for model inference but are needed for training and exploration. Importing all dependencies from `requirements.txt` would dramatically increase the package size of the model.

If the tests contain errors like the following:

    ModuleNotFoundError: No module named '<module name>'

Open `setup.py` in your editor and add the missing dependencies via the `install_requires` parameter. See the [Python docs](https://packaging.python.org/guides/distributing-packages-using-setuptools/#install-requires) for more on `install_requires`.

For example, the disaster tweets example project creates a trained Keras model with a Tensorflow backend. Its `setup.py` has the following modification:

```diff
install_requires=[
-        'whisk==0.1.24'
+        'whisk==0.1.24', 'keras>=2.3.1', 'tensorflow-cpu'
],
```

__After adding packages, re-run tox with the `-r ` option. Tox caches the project dependencies and won't re-install new dependencies by default.__

### Outdated tests

The whisk project includes default tests, but these are likely to fail when you implement your own `Model.predict` function. If `tox` is not raising `ModuleNotFoundError` errors, update the tests.

Tox runs the tests within the `tests/` directory of your project.

For example, the disaster tweets project contains the following update to `tests/test_model.py` to create a passing test:

```diff
def test_predict():
    model = Model()
-    model.predict([[1,2],[3,4]])
+    model.predict([
+        ["Theyd probably still show more life than Arsenal did yesterday, eh? EH?"],
+        ["Just happened a terrible car crash"]
+    ])
```

### 2. Build the package

With tests passing, it's time to build the package. Use the [`whisk package dist`](cli_reference.html#whisk-package-dist) command:

    $ whisk package dist

The package source distribution file is created in the `dist/` directory.

## Installing the package

You may wish to try the generated package as a sanity check before publishing on PyPi. With pip, there are two options: installing the locally generated source distribution or installing from the project's hosted Git repository.

Either way, we suggest the following flow to ensure the package is installed in an isolated environment similar to an end user experience:

```
mkdir <project_name>_test
cd <project_name>_test
python3 -m venv venv
source venv/bin/activate
```

### Install the local package archive

Type the following to install the archive you created via [`whisk package dist`](cli_reference.html#whisk-package-dist):

    pip install <path to project>/dist/<project_name>-0.1.0.tar.gz

### Install from a hosted Git repo

If your project is available at a version control hosting provider like [GitHub](https://github.com), you can install install the package via its url. For example:

    pip install git+https://github.com/<user or org name>/<project repo name>


Try the CLI:

```
<project_name> predict <your predict format>
```

Try importing the package and generating a prediction:

```py
from <package_name>.models.model import Model

Model().predict(<your predict format>)
```

## Distribute the package on PyPi

See the [Uploading your Project to PyPI](https://packaging.python.org/guides/distributing-packages-using-setuptools/#uploading-your-project-to-pypi) section of the official Python Packaging Guide for instructions on uploading your package to PyPi. Once on PyPi, anyone can install your package via `pip install <project_name>`.
