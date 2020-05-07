# {{cookiecutter.project_name}}

## Prerequisites

The following is required to run this project:

* Git (configured with a [user name and email](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup))
* Python 3.6+
* A Linux-based OS (includes OSX)

## Setup

1. Run `scripts/install.py`. The install script creates a `venv`, installs the Python dependencies specified, and initializes DVC.
2. Activate the venv: `source venv/bin/activate`
3. Download the latest data files: `dvc pull`.

## Available commands

Run:

```
inv --list
Available tasks:

app.create      Create a Heroku app for the web service.
app.destroy     Delete the Heroku app.
app.start       Start the web service serving model inference.
app.test        Run the web service unit tests.
model.predict   Invokes the model.
notebooks.run   Run a notebook from the command line.
```

For details on a specific task, use `inv --h [TASK]`. For example:

```
inv -h notebooks.run
Usage: inv[oke] [--core-opts] notebooks.run [--options] [other tasks here ...]

Docstring:
  Run a notebook from the command line.

Options:
  -r STRING, --relative-path=STRING
```

## venv

This project uses `venv` to isolate Python dependencies. To activate:

    source venv/bin/activate



{{cookiecutter.description}}

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
