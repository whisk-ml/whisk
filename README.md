# Whisk ML Project Framework

[![pypi](https://img.shields.io/pypi/v/whisk.svg)](https://pypi.python.org/pypi/whisk)

[![docs](https://readthedocs.org/projects/whisk/badge/?version=latest)](https://whisk.readthedocs.io/en/latest/?badge=latest)

Tying together the tools required to release a machine learning model can be daunting. Whisk makes building and releasing ML models easy and fun. Whisk creates a logical and flexible project structure for ML that creates reproducible results and lets you release your model to the world without becoming a software engineer.

Whisk doesn't lock you into a particular ML framework or require you to learn yet another ML packaging API. Instead, it leverages the magic of Python's ecosystem that's available to projects structured in a Pythonic-way. Whisk does the structuring while you focus on the data science.

Read more about our [beliefs](#beliefs).

## Quickstart

_Replace `demo` with the name of your ML project in the examples below._

Create the project:

```
pip install whisk
echo "Generate the directory structure, set up a venv, initialize a Git repo, and more."
whisk create demo
cd demo
source venv/bin/activate
```

Checkout the end-to-end notebook example:

```
jupyter-notebook notebooks/example.ipynb
```

The notebook shows how to save your trained model to disk, use the saved model to generate predictions, and how to load Python functions and classes from the project's `src` directory for a cleaner notebook. It's the guide rails for your own ML project.

There's a placeholder model you can invoke immediately from the command line:

```
whisk predict [[0,1],[2,3]]
```

...and a ready-to-go Flask web service:

```
whisk app start
curl --location --request POST 'http://localhost:5000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{"data":[[0, 1], [2, 3]]}'
```

Deploy the web service to Heroku (a free account is fine):

```
whisk app create demo-[INSERT YOUR NAME]
```

Create a Python package containing your model and share with the world:

```
whisk model build
echo "Installing the generated Python package"
pip install dist/demo-0.1.0.tar.gz
```

Invoke the model via the CLI:

```
demo predict [[0,1],[2,3]]
```

...and within Python code:

```py
from demo import model
model.predict([[0,1],[2,3]])
```

## Beliefs

* _A notebook isn't enough_ - A data science notebook is where experimentation starts, but you can't create a reproducible, collaborative ML project with just a `*.ipynb` file.
* _A Reproducible, collaborative project is a solved problem for classical software_ - We don't need to re-invent the wheel for machine learning projects. Instead, we need guide rails to help data scientists structure projects without forcing them to also become software engineers.
* _Python already has a good package manager_ - We don't need overly abstracted solutions to package a trained ML model. A properly structured ML project makes it easy to use _pip_ for packaging a model, making it easy for _anyone_ to benefit from your work.
* _Version control is a requirement_ - You can't have a reproducible project if the code and training data isn't in version control.
* _Docker is a heavyweight and fragile option for solving reproducibility_ - when we [explicitly declare and isolate dependencies](https://12factor.net/dependencies), we don't need to rely on the implicit existence of packages installed in a Docker container. Docker also creates a slow development flow: repeatedly restarting Docker containers is far slower than doing the same in pure Python. Python already has solid native tools for this problem.
* _Optimize for debugging_ - 90% of writing software is fixing bugs. It should be easy to debug your model logic locally.


## Credits

This package was created with Cookiecutter and the `audreyr/cookiecutter-pypackage` project template. The project template is heavily inspired by [Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science).
