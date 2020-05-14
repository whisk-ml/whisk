## Key Concepts

whisk is a ML project framework that make makes collaboration, reproducibility, and deployment "just work". Let's go through a few concepts that are important to understanding how whisk works.

### Structure

#### Project

When you run `whisk create <name>`, a **project** is automatically created for you. A project is a folder (also called [repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/about-repositories)) that holds all of the code and objects needed for your ML work. Each project created with whisk will follow a standard structure based off of the cookie cutter data science template.

This project will already have git setup. This means you can keep track of changes over time and/or push this code to a version control hosting system such as [GitHub](https://github.com/).

To check out a few examples of projects that were created with whisk, head over to the [whisk GitHub org](https://github.com/whisk-ml).

#### Virtual Environment

During the process of creating a project with whisk a virtual environment is automatically set up. This is a virtual version of a Python environment that contains specific (AKA explicit) versions of Python and all of the packages that are being used. All of these packages and their versions are listed out in `requirements.txt`.

This environment will follow your project wherever it goes. If someone elses decides to build off of your project and make changes, the environment will be identical for them as well. If you create a [package](#project-package) from your project or [deploy](#deployment) your project, the evironment will also be identical.

#### Project Code

... talking about how code sits in notebooks and other modules, but only certain modules will be use for the code production system

#### Artifacts

... artifacts are objects needed for your model to be helpful... talk about DVC as well here.

### Outputs

#### Project Package

... reference the `src` folder and how that turns into a package

#### Deployment

... talk about what deployment is

### Tools

TODO: Decide if this section is needed, or if it is going to be duplicative of the core docs

#### whisk Helper Functions

whisk contains a variety of helper functions that make developing, sharing, and deploying your ML project easy. All of these commands will look like:
```
$ whisk ...
```

To check out all of the available helper functions, run this command:

```
$ whisk --help
```
To learn more about these helper functions, check out the [cli documentation](#).
