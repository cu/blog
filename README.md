# About

[This is my blog.](https://blog.bityard.net/)

# Development/Preview Environment

The `Makefile` has some custom targets/paths in it, don't forget about those when upgrading.

Set up the virtual environment:

```
make venv
```

Run the Pelican development server:

```
make devserver
```

Use Docker to build the static site:

```
make dockerbuild
```

Get the size of the repo (minus git metadata, output dir, etc)

```
make reposize
```


# Building with Docker

```
docker run -ti --rm -v $PWD:/site -w /site python:3 bash -c 'pip install -r requirements.txt && make html'
```
