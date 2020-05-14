## Key Concepts

whisk is a ML project framework that make makes collaboration, reproducibility, and deployment "just work". Let's go through a few concepts that are important to understanding how whisk works.

### Structure

#### Project

When you run `whisk create <name>`, a **project** is automatically created for you. A project is a folder (also called [repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/about-repositories)) that holds all of the code and objects needed for your ML work. Each project created with whisk will follow a standard structure based off of the cookie cutter data science template.

This project will already have git setup. This means you can keep track of changes over time and/or push this code to a version control hosting system such as [GitHub](https://github.com/).

To check out a few examples of projects that were created with whisk, head over to the [whisk GitHub org](https://github.com/whisk-ml).

#### Virtual Environment

During the process of creating a project with whisk, a virtual environment is automatically set up. This is a virtual version of a Python environment that contains specific (AKA explicit) versions of Python and all of the packages that are being used. All of these packages and their versions are listed out in `requirements.txt`.

This environment will follow your project wherever it goes. If someone elses decides to build off of your project and make changes, the environment will be identical for them as well. If you create a [package](#project-package) from your project or [deploy](#deployment) your project, the evironment will also be identical.

#### Project Code

Your whisk project will contain a variety of different sources of code. You may start your analysis or modeling inside of [Jupyter Notebook](https://jupyter.org/) within the `/notebooks` directory. Once you have iterated to the point where you'd like to share or deploy your model, the needed code should be moved into the `/src/<name>/` directory. This directory contains all of the code that will be [packaged](#project-package) alongside your model or deployed as a web app.

#### Artifacts

As you are creating specific datasets, you'll likely want to save them and reference later as part of your model code. Also, once you land on a version of your model that peforms well, you might want to save that model for prediction as a object such as a [pickle](https://docs.python.org/3/library/pickle.html). Both the datasets and model objects will be saved as **artifacts** in your whisk project. 

These are stored in `/src/<name>/artifacts/` and their location can be referenced throughout your project with `whisk.artifact_dir`.

Note: This automatically stores all artifacts within your git repository. For very large artifacts, you'll likely want to store those objects with DVC instead. Documentation for DVC is coming soon.

### Outputs

#### Project Package

As you are developing your project and placing code in the `/src/<name>/` directory, whisk automatically converts your project into a functioning Python package. In the same way that you might `import pandas` at the beginning of an analysis, you can `import <name>` within your project and access functionality that was developed with your model. For example, your model is accessible with `from <name>.models.model import Model`.

The purpose of keeping the code packaged and available is to encourage easy collaboration. If you are ready to share your project with others, its easy to run `whisk package dist` so that others can also import and use the functionality from your project.

#### Deployment

In some cases, the model that you developed may be helpful to others as a standalone web service. This will allow yourself or other developers to access your model as service through an [API endpoint](https://smartbear.com/learn/performance-monitoring/api-endpoints/). To use this API, the developer will send a set of model inputs and will recieve your model's predictions in return.

whisk contains a few option to spin up a web service locally with `whisk app start` or on the web through [Heroku](https://www.heroku.com/) with `whisk app create <name>`

### Tools

#### whisk Helper Functions

To make project development easier, whisk contains a few helper functions. These functions contain commonly-used methods that speed up development of your model. For example:

```py
import whisk
whisk.data_dir
```
This references the location of your stored data at `/data/`.

This is not to be confused with the commands that sit alongside your packaged model code. That will be referenced with your project name. For example:

```py
from <name>.models.model import Model
model_object = Model()
```

To learn more, check out the [helper functions documentation](#).

#### whisk CLI

whisk contains a command line interface (CLI) that make developing, sharing, and deploying your ML project easy. All of these commands will look like:
```
$ whisk ...
```

To check out all of the available CLI commands, run this command:

```
$ whisk --help
```
To learn more about these CLI commands, check out the [CLI documentation](cli_reference.html).
