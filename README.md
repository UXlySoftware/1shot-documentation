# 1Shot Docs
Sphinx docs repo which build the user docs for [1shotapi.com](https://1shotapi.com). 

## Build instructions
Replace example path with correct path for your filesystem.

To build the documentation:

```sh
docker run --rm -v ~/code/1shot-documentation:/docs sphinxdoc/sphinx make html
```

To serve the documentation locally:

```sh
docker run -d --rm -p 8080:8080 --name sphinx -v ~/code/1shot-documentation/docs/:/root python:3.12 python -m http.server 8080 -d /root
```