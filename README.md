# Building with Docker

```
docker run -ti --rm -v $PWD:/site -w /site python:3.9 bash

pip install -r requirements.txt
make html
```
