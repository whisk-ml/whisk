# Heroku Deployment

[Heroku](https://heroku.com) is a cloud platform as a service supporting several programming languages, [including Python](https://devcenter.heroku.com/categories/python-support). Heroku is the default option for model deployment as a web service for whisk. In most cases, Heroku is free for proof-of-concept models and a low-cost, less complex approach compared to solutions like AWS Sagemaker in the long-run.

To deploy the web service residing in the `app/` directory to Heroku, type [`whisk app create [NAME OF THE HEROKU APP]`](cli_reference.html#whisk-app-create).

## Heroku ML Model Gotchas

Your project may require a couple of slight modifications to successfully deploy to Heroku. Below is a list of common issues.

### Max Slug Size Limit

Heroku has a [maximum slug size of 500 MB](https://devcenter.heroku.com/articles/slug-compiler#slug-size) (after compression). If you project contains large dependencies (like Tensorflow), you could exceed this limit.

### Tensorflow

The Tensorflow library is greater than 500 MB and exceeds the Heroku slug size limit by itself. Use `tensorflow-cpu` as it consumes < 150 MB of disk space. Heroku also does not offer GPUs so there is loss in functionality.

### NLTK

If you are using NLTK, add a `nltk.txt` file to the project root directory with a list of corpora to download. See the [Heroku NLTK docs](https://devcenter.heroku.com/articles/python-nltk) for more information.

### .slugignore

The project contains a `.slugignore` file that removes the `data/` and `notebooks/` directories before the buildpack runs. This reduces the slug size.

### Python version

Specify a Python version to use on Heroku by adding a `runtime.txt` file to your project root. [Learn more about specifying a Python runtime](https://devcenter.heroku.com/articles/python-runtimes) on Heroku.
