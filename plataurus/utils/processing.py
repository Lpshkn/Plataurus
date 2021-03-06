import re
from slovnet import Morph
from pymorphy2 import MorphAnalyzer
from razdel import tokenize

SWORDS_LITE = {'и', 'в', 'во', 'не', 'что', 'он', 'на', 'я', 'с', 'со', 'как', 'а', 'то', 'все', 'она', 'так',
               'его', 'но', 'да', 'ты', 'к', 'ко', 'у', 'же', 'вы', 'за', 'бы', 'по', 'ее', 'мне', 'её',
               'вот', 'от', 'меня', 'еще', 'нет', 'о', 'из', 'ему', 'ли', 'если', 'уже', 'или', 'ни',
               'него', 'до', 'вас', 'нибудь', 'уж', 'вам', 'всё',
               'ведь', 'там', 'потом', 'себя', 'ничего', 'ей', 'они', 'тут', 'где', 'надо', 'ней',
               'для', 'мы', 'тебя', 'их', 'чем', 'сам', 'без', 'раз', 'тоже', 'себе',
               'под', 'ж', 'кто', 'этот', 'того', 'какой', 'совсем', 'ним',
               'здесь', 'этом', 'один', 'мой', 'тем', 'нее', 'куда', 'зачем',
               'всех', 'никогда', 'можно', 'при', 'два', 'об', 'другой', 'хоть', 'после', 'над', 'больше',
               'тот', 'через', 'эти', 'нас', 'про', 'всего', 'них', 'какая', 'много', 'разве', 'три', 'эту', 'моя',
               'свою', 'этой', 'это', 'перед', 'иногда', 'лучше', 'чуть', 'том', 'нельзя', 'такой',
               'им', 'всю', 'куда-нибудь', 'как-нибудь', 'где-нибудь', 'когда-нибудь', 'чем-нибудь', 'что-нибудь',
               'кто-то', 'что-то', 'где-то', 'когда-то'}

STOPWORDS = re.compile(rf"\b({'|'.join(list(SWORDS_LITE))})\b", re.IGNORECASE)


def process_sentence(morph: Morph, sentence: str):
    sentence = sentence.lower()
    sentence = re.sub(r'[\s]+', r' ', sentence).strip()
    sentence = re.sub(r'[^a-zа-яё -]', '', sentence)

    pymorph = MorphAnalyzer()
    tokens = [[_.text for _ in tokenize(sentence) if _.text not in SWORDS_LITE]]

    markup = next(morph.map(tokens))
    words = []
    for token in markup.tokens:
        word = token.text
        parsed_word = pymorph.parse(word)[0].normal_form
        words.append(parsed_word)

    return " ".join(words)
