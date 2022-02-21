FROM snakepacker/python:all as builder

RUN python3.8 -m venv /usr/share/python3/venv \
 && /usr/share/python3/venv/bin/pip install -U pip

COPY . /mnt/
RUN /usr/share/python3/venv/bin/pip install /mnt/

RUN apt-get update && \
	apt-get upgrade -y && \
	apt-get install -y wget

FROM snakepacker/python:3.8
MAINTAINER lpshkn

COPY --from=builder /usr/share/python3/venv /usr/share/python3/venv
COPY --from=builder /usr/bin/wget /usr/bin/wget
RUN ln -snf /usr/share/python3/venv/bin/plataurus* /usr/local/bin/
RUN mkdir -p /data && \
    wget -P /data/ "https://storage.yandexcloud.net/natasha-navec/packs/navec_news_v1_1B_250K_300d_100q.tar" && \
    wget -P /data/ "https://storage.yandexcloud.net/natasha-slovnet/packs/slovnet_morph_news_v1.tar"

ENV NAVEC_ARCHIVE=/data/navec_news_v1_1B_250K_300d_100q.tar
ENV MORPH_ARCHIVE=/data/slovnet_morph_news_v1.tar

ENTRYPOINT ["plataurus-web"]