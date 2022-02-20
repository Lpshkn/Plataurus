DOCKER := env docker
PYTHON := env python3
COMPOSE := env docker-compose

DATA_DIR := data

help:
	@exit 0

# Data preloading
preload-data:
	[ -f $(DATA_DIR)/navec_news_v1_1B_250K_300d_100q.tar ] || wget https://storage.yandexcloud.net/natasha-navec/packs/navec_news_v1_1B_250K_300d_100q.tar -P $(DATA_DIR)
	[ -f $(DATA_DIR)/slovnet_morph_news_v1.tar ] || wget https://storage.yandexcloud.net/natasha-slovnet/packs/slovnet_morph_news_v1.tar -P $(DATA_DIR)

run-prod:
	@echo "run-prod coming soon"
