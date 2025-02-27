<div align="center">
  <img src="source/_static/1shot-logo.svg" alt="1Shot" />
</div>

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

## Converting .mov to .gifs

Use ffmpeg to convert screen recordings into embeddable gif formats:

```
docker run --rm -v ~/code/1shot-documentation/source/_static/:/root linuxserver/ffmpeg -i /root/org-creation/create-org-recording.mov -vf "fps=10,scale=640:-1:flags=lanczos" /root/org-creation/create-org-recording.gif
```

## Themes

You can play with new themes using the supplied [Dockerfile](./Dockerfile). Use `pip` to install the necessary theme package into a local docker image, then change the `html_theme` option in the [conf.py](./source/conf.py) to point to the correct theme. Run the build command above using the new local docker image. 