# HTTP Web Service

This is an HTTP API skeleton to run model inference. The web app is powered by Flask.

## Running the web app

From the project root:

```
inv app.start
```

The app is available at http://localhost:5000/.

If the source code (``*.py` files) is updated, the app is reloaded automatically in development mode.

## Example Usage

```
curl --location --request POST 'http://localhost:5000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{"data":[[0, 1], [2, 3]]}'
```

```
[
  2,
  2
]
```

## Creating an app on Heroku

From the project root:

```
inv app.create [HEROKU APP NAME]
```
