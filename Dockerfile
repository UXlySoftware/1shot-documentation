FROM sphinxdoc/sphinx

COPY source/requirements.txt .

RUN python -m pip install -r requirements.txt