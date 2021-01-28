# FastAPI example

This is an example of creating a simple ML application with FastAPI.

## docker way

```
$ docker-compose up
```

## development

setup

```
$ poetry install
```

train

```
$ cd app
$ poetry run python train.py
```

start webapp

```
$ cd app
$ poetry run uvicorn main:app --reload
```

run tests

```
$ cd app
$ poetry run pytest
```

## links

- Slide
  - [さよならFlask ようこそFastAPI](https://speakerdeck.com/amaotone/goodbye-flask-welcome-fastapi)
- Framework
  - [FastAPI](https://fastapi.tiangolo.com/ja/)
  - [Pydantic](https://pydantic-docs.helpmanual.io/)
- Dataset
  - [palmerpenguins](https://allisonhorst.github.io/palmerpenguins/)
