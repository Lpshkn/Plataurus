from os import getenv
from os.path import dirname, join


class Config:
    # Paths to archives where models of Natasha's Slovnet are storing
    navec_archive = getenv("NAVEC_ARCHIVE", join(dirname(dirname(__file__)),
                                                 "data/navec_news_v1_1B_250K_300d_100q.tar"))
    morph_archive = getenv("MORPH_ARCHIVE", join(dirname(dirname(__file__)),
                                                 "data/slovnet_morph_news_v1.tar"))

    class Logging:
        format = "%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"

    class Application:
        # Parameters of a aiohttp server
        host = '0.0.0.0'
        port = '8090'

        # Default texts for text areas of index.html
        default_first_text = "Мама мыла раму и не раз. Она открыта ко многим предложениям. В принципе, в этом нет " \
                             "ничего такого. Лошадка была красивая, но не умела разговаривать. Что ж, я не могу " \
                             "предложить вам ничего более. Оставайтесь на чай, мадам, у нас будет весело! " \
                             "Что бы вы не говорили, всё будет сказано против вас. Досвидания, мой друг."

        default_second_text = "Она открыта ко многим предложениям. В принципе, в этом нет ничего такого. Я бы не " \
                              "сказал, что космос многое изменил. Вы правы, это выглядит вызывающе. Лошадка была " \
                              "красивая, но не умела разговаривать. Что ж, я не могу предложить вам ничего более. " \
                              "Правда была в том, что это ложь. До свидания, мой друг."
