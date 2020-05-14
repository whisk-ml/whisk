# Project Structure Reference

A project created with [`whisk create`](cli_reference.html#whisk-create) generates the following directory structure:
<!-- Generate this with:
 tree whisk/template/\{\{\ cookiecutter.repo_name\ \}\}/
-->

    ├── MANIFEST.in           <- Include required non-*py files in the source distribution.
    │                            See https://packaging.python.org/guides/using-manifest-in/
    │
    ├── README.md             <- The top-level README for developers using this project.
    │
    ├── app                   <- Flask app for serving the model inference web service.
    │
    ├── data
    │   ├── external          <- Data from third party sources.
    │   ├── interim           <- Intermediate data that has been transformed.
    │   ├── processed         <- The final, canonical data sets for modeling.
    │   └── raw               <- The original, immutable data dump.
    │
    ├── docs                  <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── notebooks             <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                            the creator's initials, and a short `-` delimited description, e.g.
    │                            `1.0-jqp-initial-data-exploration`.             
    │
    ├── references            <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports               <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures           <- Generated graphics and figures to be used in reporting.
    │
    ├── requirements.txt      <- The requirements file for reproducing the analysis environment, e.g.
    │                            generated with `pip freeze > requirements.txt`.
    │
    ├── setup.py              <- Makes project pip installable (pip install -e .) so src can be imported and
    │                           packaged for distribution.
    ├── src
    │   └── [PROJECT NAME]    <- The top-level module for this project (import [PROJECT NAME]).
    │       ├── artifacts     <- Saved artifacts required for generating predictions (like trained models, classifiers, etc.).
    │       ├── cli           <- Command Line Interface (CLI) commands for your project. Powered by https://click.palletsprojects.com/en/7.x/.
    │       ├── data          <- Scripts to download or generate data.
    │       ├── features      <- Scripts to turn raw data into features for modeling.
    │       └── models        <- Scripts to train models and then use trained models to make predictions.
    │           │              
    └           └── model.py  <- Scaffolded model class for use with whisk.
    │       └── visualization <- Scripts to create exploratory and results oriented visualizations.
    │
    ├── tests                 <- Tests to ensure the project works as expected.
    │                            See https://docs.pytest.org/en/latest/.
    │   ├── test_cli.py
    │   └── test_model.py
    │
    ├── tox.ini               <- tox file to test the package against multiple Python environments.
    │                            See tox.testrun.org.
    │
    ├── venv                  <- The Python3 virtual environment for the project.
    │
    └── whisk_commands        <- Add custom `whisk` CLI commands and override existing ones.
        │                        Powered by https://click.palletsprojects.com/en/7.x/.
        └── app.py

This structure is inspired by [Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science) and [Cookiecutter PyPackage](https://github.com/audreyr/cookiecutter-pypackage).
