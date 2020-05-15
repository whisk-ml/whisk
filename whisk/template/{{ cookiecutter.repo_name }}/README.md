# {{cookiecutter.project_name}}

This readme was auto-generated using [whisk](https://github.com/whisk-ml/whisk). whisk creates a logical and flexible project structure for ML with reproducible results and lets you release your model to the world without becoming a software engineer.

Once your project is setup, edit this readme directly to add context and documentation for your project.

## Prerequisites

The following is required to run this project:

* Git (configured with a [user name and email](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup))
* Python 3.6+
* A Linux-based OS (includes OSX)

## Setup

After cloning this repo and `cd {{cookiecutter.project_name}}`:

1. If you haven't yet installed whisk, run `pip install whisk`
2. Run `whisk setup`. The install script creates a `venv`, installs the Python dependencies specified, and initializes DVC.
3. Activate the venv: `source venv/bin/activate`
4. If DVC is used, Download the latest data files: `dvc pull`.

To learn more about whisk, here are a few helpful doc pages:
* [A Quick Tour of whisk](https://whisk.readthedocs.io/en/latest/tour_of_whisk.html)
* [Key Concepts](https://whisk.readthedocs.io/en/latest/key_concepts.html)
* [Project Structure](https://whisk.readthedocs.io/en/latest/project_structure.html)

--------

<p><small>Project built with the <a target="_blank" href="https://github.com/whisk-ml/whisk">whisk ML project framework</a> based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
