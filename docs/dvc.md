# Data Version Control

Machine Learning projects require both code and data to build a model. Both the code and the data needs to be version controlled to ensure that results are reproducible at any point in time. However, data presents two version control challenges:

1. Large datasets - often the training dataset is too large to fit in a Git repository.
2. Slow pipeline stages - Training a model on a large dataset can take a significant amount of time. It's painful to be forced to retrain a model if the training data, code, and outputs are up-to-date already.

Data Version Control ([DVC](https://dvc.org/)) is a Python package that solves the above ML-specific project challenges and is installed as a dependency within whisk projects. It's a lightweight, flexible tool that aligns closely with git commands.

## Enabling DVC

Type [`whisk dvc setup`](cli_reference.html#whisk-dvc-setup) to enable DVC within your project. After setup completes, you need a place to store your data. whisk includes a set of commands to automate the setup of an S3 [DVC remote](https://dvc.org/doc/command-reference/remote). To create a remote:

```
whisk s3 create
whisk dvc remote-add
```

This creates an Amazon S3 bucket named `whisk-<project_name>` and creates a DVC remote that uses the S3 bucket.

## Using DVC

The DVC website has [excellent documentation](https://dvc.org/doc) on using DVC. Please refer to their website.

## Example Project

The [Real or Not? NLP with Disaster Tweets](https://github.com/whisk-ml/disaster_tweets) whisk project uses DVC to version control the data download and training stages. This keeps the large dataset and model artifacts outside of version control. As the training stage takes ~20 minutes on a laptop, this can save a significant amount of time when bootstrapping the project. New users can immediately begin using the model after running `dvc pull` versus waiting for the training to complete.

## Heroku deployment

If your app stores artifacts in DVC, those files will need be available by default when the app is [deployed to Heroku](heroku.html). To ensure the artifacts are available, we suggest adding a `.profile` file to the root of your project to pull these artifacts.

[Real or Not? NLP with Disaster Tweets](https://github.com/whisk-ml/disaster_tweets/blob/master/.profile) uses the following `.profile` to do this:

    # .profile

    git init # Needed as dvc pull will not work if this isn't a Git repo.
    dvc pull train.dvc # Grab only the training output, not all files (don't need raw data)

Heroku [runs the .profile](https://devcenter.heroku.com/articles/dynos#the-profile-file) file before executing the dyno’s command. This ensure that every dyno type has access to the needed model artifacts.

## Python Package

As long as you build the package locally or on a CI server with the DVC files in place, the distribution archive will include any DVC artifacts within `src/<project_name>/artifacts`. However, to support pip installs via a Git repo url (`pip install git+https://url-to-your-git-repo`), you need to get the DVC files as part of the package setup process.

The [Real or Not? NLP with Disaster Tweets](https://github.com/whisk-ml/disaster_tweets/blob/master/setup.py) `setup.py` file shows how to perform [dvc get](https://dvc.org/doc/command-reference/get) as part of the package setup.

## Public Read-only DVC Remote

If you share a public project on GitHub that contains files in a DVC remote, other developers will not be able to access those files by default. To enable read-only access to the DVC remote, run the following commands within your whisk project:

    whisk s3 make-public
    dvc remote add --local s3 s3://whisk-<project_name>/
    dvc remote add -d s3_http https://whisk-<project_name>.s3.amazonaws.com/
    dvc remote default s3 --local
    # Then commit changes to Git...

This adds a public read-only policy to the S3 bucket used for the DVC remote, creates a local (visible only to you) remote with the S3 bucket, adds the read-only remote for everyone, and sets your remote to S3 (versus http). In short, it behaves like a public GitHub repository.

You can revert the public policy with:

    whisk s3 delete-policy
