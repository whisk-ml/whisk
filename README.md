# whisk: The easy-bake ML project structure

[![pypi](https://img.shields.io/pypi/v/whisk.svg)](https://pypi.python.org/pypi/whisk)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/whisk)](https://pypi.python.org/pypi/whisk)
[![docs](https://readthedocs.org/projects/whisk/badge/?version=latest)](https://whisk.readthedocs.io/en/latest/?badge=latest)

**[whisk](https://whisk.readthedocs.io/en/latest/) is a ML project framework that make makes collaboration, reproducibility, and deployment "just work".**

Tying together the tools required to release a machine learning model can be daunting. Whisk makes building and releasing ML models easy and fun. Whisk creates a logical and flexible project structure for ML with reproducible results and lets you release your model to the world without becoming a software engineer.

Whisk doesn't lock you into a particular ML framework or require you to learn yet another ML packaging API. Instead, it leverages the magic of Python's ecosystem that's available to projects structured in a Pythonic-way. Whisk does the structuring while you focus on the data science.

Read more about our [beliefs](#beliefs).

## Quickstart

_Replace `demo` with the name of your ML project in the examples below._

### Create a project for the model

Create the project with whisk:

```
$ pip install whisk
$ echo "Generate the directory structure, set up a venv, initialize a Git repo, and more."
$ whisk create demo
$ cd demo
$ source venv/bin/activate
```

Take a quick tour the project you just created:

```
$ jupyter-notebook notebooks/getting_started.ipynb
```

The notebook shows how to save your trained model to disk, use the saved model to generate predictions, how to load Python functions and classes from the project's `src` directory for a cleaner notebook, and more. It's the guide rails for your own ML project.

### Test the model

Once you've created a model with whisk, it's easy to test locally.

There's a placeholder model you can invoke immediately from the command line:

```
$ demo predict [[0,1],[2,3]]
[2, 2]
```

...and within Python code:

```py
from demo.models.model import Model
model = Model()
model.predict([[0,1],[2,3]])
```

### Share and deploy the model

After you develop and test your model, it's time to share.

Create a **Python package** containing your model and share with the world:

```
$ whisk package dist
Python Package created in /Users/dlite/projects/whisk_examples/demo/dist:
demo-0.1.0.tar.gz

$ pip install dist/demo-0.1.0.tar.gz
```

... or create a **ready-to-go Flask web service**:

```
$ whisk app start
$ curl --location --request POST 'http://localhost:5000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{"data":[[0, 1], [2, 3]]}'
```

... and **deploy the web service to Heroku** ([a free account is fine](https://signup.heroku.com/)):

```
$ whisk app create demo-[INSERT YOUR NAME]
```

## Whisk CLI Commands

To see a list of available whisk commands and command groups:

    whisk --help

You can view help on specific command groups like this:

    whisk app --help

## Beliefs

* **A Reproducible, collaborative project is a solved problem for classical software** - We don't need to re-invent the wheel for machine learning projects. Instead, we need guide rails to help data scientists structure projects without forcing them to also become software engineers.
* **A notebook is great for exploring, but not for production** - A data science notebook is where experimentation starts, but you can't create a reproducible, collaborative ML project with just a `*.ipynb` file.
* **Python already has a good package manager** - We don't need overly abstracted solutions to package a trained ML model. A properly structured ML project makes it easy to use _pip_ for packaging a model, making it easy for _anyone_ to benefit from your work.
* **Version control is a requirement** - You can't have a reproducible project if the code and training data isn't in version control.
* **Docker and Kubernetes are usually not needed** - when we [explicitly declare and isolate dependencies](https://12factor.net/dependencies), we don't need to rely on the implicit existence of packages installed in a Docker container. Docker also creates a slow development flow: repeatedly restarting Docker containers is far slower than doing the same in pure Python. Python already has solid native tools for this problem.
* **Optimize for debugging** - 90% of writing software is fixing bugs. It should be easy to debug your model logic locally. You should be able to search your error and find results, not sift through custom package source code.

## Examples

Check out whisk example projects in [the whisk GitHub organization](https://github.com/whisk-ml).

## Contributing

Want to help build whisk? Check out our [contributing documentation](https://github.com/whisk-ml/whisk/blob/master/docs/contributing.md).

## Credits

This package was created with Cookiecutter and the `audreyr/cookiecutter-pypackage` project template. The project template is heavily inspired by [Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science).
