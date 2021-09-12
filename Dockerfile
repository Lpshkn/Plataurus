FROM python:3.9.2-slim-buster
MAINTAINER lpshkn

COPY requirements.txt /tmp
RUN python3 -m pip install --upgrade pip && pip3 install -r /tmp/requirements.txt

COPY . /plataurus
WORKDIR /plataurus

ENTRYPOINT ["python3", "main.py"]