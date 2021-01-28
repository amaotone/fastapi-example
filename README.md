# FastAPI example

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