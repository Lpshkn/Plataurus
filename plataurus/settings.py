from os import getenv


class Config:
    # Paths to archives where models of Natasha's Slovnet are storing
    navec_archive = getenv("NAVEC_ARCHIVE", "./../data/navec_news_v1_1B_250K_300d_100q.tar")
    morph_archive = getenv("MORPH_ARCHIVE", "./../data/slovnet_morph_news_v1.tar")

    class Logging:
        format = "%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"

    class Application:
        # Parameters of a aiohttp server
        host = '0.0.0.0'
        port = '8090'

        # Initializers of text areas
        FIRST_TEXT = "Мама мыла раму и не раз. Она открыта ко многим предложениям. В принципе, в этом нет ничего " \
                     "такого. Лошадка была красивая, но не умела разговаривать. Что ж, я не могу предложить вам " \
                     "ничего более. Оставайтесь на чай, мадам, у нас будет весело! Что бы вы не говорили, всё будет " \
                     "сказано против вас. Досвидания, мой друг."

        SECOND_TEXT = "Она открыта ко многим предложениям. В принципе, в этом нет ничего такого. Я бы не сказал, что " \
                      "космос многое изменил. Вы правы, это выглядит вызывающе. Лошадка была красивая, но не умела " \
                      "разговаривать. Что ж, я не могу предложить вам ничего более. Правда была в том, что это ложь. " \
                      "До свидания, мой друг."
