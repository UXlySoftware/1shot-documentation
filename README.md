# 1shot-documentation
Sphinx docs repo which build the user docs for [1shotapi.com](https://1shotapi.com). 

## Build instructions
Replace example path with correct path for your filesystem.

To build the documentation:

```sh
docker run --rm -v /home/todd/code/1shot-documentation:/docs sphinxdoc/sphinx make html
```

To serve the documentation locally:

```sh
docker run -it --rm -p 8080:8080 --name sphinx -v /home/todd/code/1shot-documentation/build/html/:/root python:3.12 python -m http.server 8080 -d /root
```