## Key Concepts

whisk is a ML project framework that makes collaboration, reproducibility, and deployment "just work". Let's go through a few concepts that are important to understanding how whisk makes this happen.

### Structure

#### Directory Structure

When you run [`whisk create <project_name>`](cli_reference.html#whisk-create), a directory named <project_name> is created. The directory follows a [data science-flavored Python project structure](project_structure.html).

The directory is also a Git [repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/about-repositories), pre-initialized with a first commit that contains the directory structure. This means you can keep track of changes over time and/or push this code to a version control hosting system such as [GitHub](https://github.com/).

To check out a few examples of projects that were created with whisk, head over to the [whisk GitHub org](https://github.com/whisk-ml).

#### Virtual Environment

A [Python3 virtual environment](https://docs.python.org/3/library/venv.html) is created as well when you run [`whisk create <project_name>`](cli_reference.html#whisk-create). This is a virtual version of a Python environment that contains specific (AKA explicit) versions of packages that are being used. All of these packages and their versions are listed in `requirements.txt`.

This environment will follow your project wherever it goes. If someone else decides to build off of your project and make changes, the environment will be identical for them as well.

#### Project Code

Your whisk project will contain a variety of different sources of code. You may start your analysis or modeling inside a [Jupyter Notebook](https://jupyter.org/) within the `notebooks/` directory. When you are ready to collaborate or deploy your model, the needed code should be moved into the `src/<project_name>/` directory. This directory contains all of the code that will be [packaged](#project-package) alongside your model or deployed as a web app.

#### Training Data

Raw training data should be version-controlled alongside the project code to ensure your experiments are reproducible. Place training data within the `data/` directory of your project. You can access the location of this directory via `<project_name>.artifacts_dir`.

#### Artifacts

Once you land on a version of your model that performs well, you'll want to save the model to disk with a library like [pickle](https://docs.python.org/3/library/pickle.html).

These should be stored in `src/<project_name>/artifacts/` and their location can be referenced throughout your project with `<project_name>.artifact_dir`. These artifacts are automatically included in your model's Python package.

### Outputs

Your model can be released as both a Python Package and deployed to Heroku as a web service.

#### Python Package

As you are developing your project and placing code in the `src/<project_name>/` directory, whisk automatically converts your project into a functioning Python package. In the same way that you might `import pandas` at the beginning of an analysis, you can `import <project_name>` within your project and access functionality that was developed with your model. For example, your model is accessible with `from <project_name>.models.model import Model`.

The purpose of keeping the code packaged and available is to encourage easy collaboration. If you are ready to share your project with others, its easy to run [`whisk package dist`](cli_reference.html#whisk-package-dist) so that others can also import and use the functionality from your project.

#### Deployment

The model that you developed may be helpful to others as a standalone web service. This will allow yourself or other developers to access your model as service through an [API endpoint](https://smartbear.com/learn/performance-monitoring/api-endpoints/). To use this API, the developer will send a set of model inputs and will receive your model's predictions in return.

You can run the web service locally with [`whisk app start`](cli_reference.html#whisk-app-start) and deploy to [Heroku](https://www.heroku.com/) with [`whisk app create <project_name>`](cli_reference.html#whisk-app-create).

### Tools

#### Helper Functions

To make project development easier, whisk contains a few helper functions. These functions contain commonly-used methods that speed up development of your model. For example:

```py
import <project_name>
<project_name>.data_dir # location of your stored data at `data/`.
<project_name>.artifact_dir # location of the artifacts (ie trained models saved to disk) at `src/<project_name>/artifacts`
```

This is not to be confused with the commands that sit alongside your packaged model code. That will be referenced with your project name. For example:

```py
from <project_name>.models.model import Model
model_object = Model()
```

#### CLI

whisk contains a command line interface (CLI) that make developing, sharing, and deploying your ML project easy. All of these commands start with `whisk`. To learn more about these CLI commands, check out the [CLI documentation](cli_reference.html).
