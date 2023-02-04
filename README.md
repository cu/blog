# About

[This is my blog.](https://blog.bityard.net/)

# Development/Preview Environment

Set up the virtual environment:

```
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install wheel
pip install -r requirements.txt
```

Run the Pelican development server:

```
make devserver
```

# Building with Docker

```
docker run -ti --rm -v $PWD:/site -w /site python:3.9 bash

pip install -r requirements.txt
make html
```
