FROM python:3.9.2-slim-buster
MAINTAINER lpshkn

COPY requirements.txt /tmp
RUN python3 -m pip install --upgrade pip && pip3 install -r /tmp/requirements.txt

ENV NAVEC_ARCHIVE=/plataurus/models/navec_news_v1_1B_250K_300d_100q.tar
ENV MORPH_ARCHIVE=/plataurus/models/slovnet_morph_news_v1.tar

COPY . /plataurus
WORKDIR /plataurus

RUN mkdir /plataurus/models &&
    wget -p /plataurus/models/ "https://storage.yandexcloud.net/natasha-navec/packs/navec_news_v1_1B_250K_300d_100q.tar" &&
    wget -p /plataurus/models/ "https://storage.yandexcloud.net/natasha-slovnet/packs/slovnet_morph_news_v1.tar"

ENTRYPOINT ["python3", "main.py"]