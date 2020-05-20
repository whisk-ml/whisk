# {{cookiecutter.project_name}}

This readme was auto-generated using [whisk](https://github.com/whisk-ml/whisk). whisk creates a logical and flexible project structure for ML with reproducible results and lets you release your model to the world without becoming a software engineer.

Once your project is setup, edit this readme directly to add context and documentation for your project.

## Prerequisites

The following is required to run this project:

* Git (configured with a [user name and email](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup))
* Python 3.6+
* A Linux-based OS (includes OSX)

## Setup

After cloning this repo, perform the following steps to initialize the project:

    cd {{cookiecutter.project_name}}
    pip install whisk
    whisk setup
    source venv/bin/activate

If DVC is used, download the latest data files: `dvc pull`.

The steps above change to the project directory, install whisk, and setup the project environment.

To learn more about whisk, here are a few helpful doc pages:
* [A Quick Tour of whisk](https://docs.whisk-ml.org.io/en/latest/tour_of_whisk.html)
* [Key Concepts](https://docs.whisk-ml.org.io/en/latest/key_concepts.html)
* [Project Structure](https://docs.whisk-ml.org.io/en/latest/project_structure.html)

--------

<p><small>Project built with the <a target="_blank" href="https://github.com/whisk-ml/whisk">whisk ML project framework</a>.
