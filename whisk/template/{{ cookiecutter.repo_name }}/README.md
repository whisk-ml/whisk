# {{cookiecutter.project_name}}

This readme was auto-generated using `whisk`. `whisk` creates a logical and flexible project structure for ML with reproducible results and lets you release your model to the world without becoming a software engineer. 

Once your project is setup, edit this readme directly to add context and documentation for your project.

## Prerequisites

The following is required to run this project:

* Git (configured with a [user name and email](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup))
* Python 3.6+
* A Linux-based OS (includes OSX)

## Setup

After cloning this repo and `cd {{cookiecutter.project_name}}`:

1. If you haven't yet installed `whisk`, run `pip install whisk`
2. Run `whisk setup`. The install script creates a `venv`, installs the Python dependencies specified, and initializes DVC.
3. Activate the venv: `source venv/bin/activate`
4. If DVC is used, Download the latest data files: `dvc pull`.

## Whisk CLI Commands

To see a list of available whisk commands and command groups:

```
whisk --help
```

You can view help on specific command groups like this:

```
whisk app --help
```

## {{cookiecutter.project_name}} CLI Commands

{{cookiecutter.project_name}} also allows for prediction directly in the CLI:

```
{{cookiecutter.project_name}} predict <input_format>
```

## Accessing {{cookiecutter.project_name}} in Python

{{cookiecutter.project_name}} also allows for prediction directly in the CLI:

```
from {{cookiecutter.project_name}}.models.model import Model

model.predict(<input_format>)
```


Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
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
    ├── src/{{cookiecutter.project_name}}      <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── artifacts      <- Artifacts needed use by the source code
    │   │   
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   └── model.py   <- Template model class for use with whisk
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    ├── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
    │
    └─── whisk_commands
        └── app.py         <- Script to add or change whisk commands for your project


--------

<p><small>Project built with the <a target="_blank" href="https://github.com/whisk-ml/whisk">whisk ML project framework</a> based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
