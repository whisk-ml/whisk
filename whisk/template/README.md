# Booklet Flow Data Science Project Template

[![booklet flow](https://circleci.com/gh/itsderek23/cookiecutter-data-science.svg?style=svg)](https://app.circleci.com/pipelines/github/itsderek23/cookiecutter-data-science?branch=master)

This is a fork of the excellent [Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science), focusing on creating a smooth CD4ML experience for data scientists.

## Requirements

 - Python 3.5 or greater
 - Git
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip:

``` bash
$ pip install cookiecutter
```

## Optional

[Direnv](https://direnv.net/) to load project-specific environment variables plus auto activate and deactivate the `venv`.

### To start a new project, run:
------------

    cookiecutter https://github.com/itsderek23/cookiecutter-data-science

In addition to creating the directory structure (see below), projects are pre-initialized with the following:

* A Git repo
* A [venv](https://docs.python.org/3/library/venv.html) named `venv`
* [DVC](https://dvc.org/) with [git hooks](https://dvc.org/doc/command-reference/install).
* [Installs](https://anbasile.github.io/posts/2017-06-25-jupyter-venv/) an `ipykernel` kernel for use in Jupyter Notebooks w/name=`project_name`.

### The resulting directory structure
------------

The directory structure of your new project looks like this:

```
├── LICENSE
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── .envrc             <- Load project-specific environment variables plus
│                         auto activate and deactivate the venv with https://direnv.net/.
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
```

### Installing development requirements

    pip install -r requirements.txt

### Running tests

    pytest -s
