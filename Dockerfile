FROM python:3.9.2-slim-buster
MAINTAINER lpshkn

COPY requirements.txt /tmp
RUN apt-get update && apt-get install -y wget
RUN python3 -m pip install --upgrade pip && pip3 install -r /tmp/requirements.txt

ENV NAVEC_ARCHIVE=/models/navec_news_v1_1B_250K_300d_100q.tar
ENV MORPH_ARCHIVE=/models/slovnet_morph_news_v1.tar

RUN mkdir -p /models && \
    wget -P /models/ "https://storage.yandexcloud.net/natasha-navec/packs/navec_news_v1_1B_250K_300d_100q.tar" && \
    wget -P /models/ "https://storage.yandexcloud.net/natasha-slovnet/packs/slovnet_morph_news_v1.tar"

COPY . /plataurus
WORKDIR /plataurus

ENTRYPOINT ["python3", "main.py"]