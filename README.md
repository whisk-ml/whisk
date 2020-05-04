# Whisk Machine Learning Project Framework

[![pypi](https://img.shields.io/pypi/v/whisk.svg)](https://pypi.python.org/pypi/whisk)

[![docs](https://readthedocs.org/projects/whisk/badge/?version=latest)](https://whisk.readthedocs.io/en/latest/?badge=latest)

## Beliefs

* _A notebook isn't enough_ - A data science notebook is where experimentation starts, but you can't create a reproducible, collaborative ML project with just a `*.ipynb` file.
* _A Reproducible, collaborative project is a solved problem for classical software_ - We don't need to re-invent the wheel for machine learning projects. Instead, we need guide rails to help data scientists structure projects without forcing them to also become software engineers.
* _Python already has a good package manager_ - We don't need overly abstracted solutions to package a trained ML model. A properly structured ML project makes it easy to use _pip_ for packaging a model, making it easy for _anyone_ to benefit from your work.
* _Version control is a requirement_ - You can't have a reproducible project if the code and training data isn't in version control.
* _Docker is a heavyweight and fragile option for solving reproducibility_ - when we [explicitly declare and isolate dependencies](https://12factor.net/dependencies), we don't need to rely on the implicit existence of system-wide packages installed in a Docker container. Docker also creates a slow development flow: repeatedly restarting Docker containers is far slower than doing the same in pure Python. 


## Credits

This package was created with Cookiecutter and the `audreyr/cookiecutter-pypackage` project template.
