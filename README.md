# 1shot-documentation
Documentation for 1Shot

## Docker environment

To build the documentation, run:

```sh
docker run --rm -v /home/todd/code/1shot-documentation:/docs sphinxdoc/sphinx make html
```

To serve the documentation, run:

```sh
docker run -it -p 8080:8080 --name sphinx -v /home/todd/code/1shot-documentation/build/html/:/root python:3.12 python -m http.server 8080 -d /root
```