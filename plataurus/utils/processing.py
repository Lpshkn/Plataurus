from slovnet import Morph
from pymorphy2 import MorphAnalyzer
from razdel import tokenize


def process_sentence(morph: Morph, sentence: str):
    pymorph = MorphAnalyzer()
    tokens = [[_.text.lower() for _ in tokenize(sentence)]]

    markup = next(morph.map(tokens))
    words = []
    for token in markup.tokens:
        if token.pos == 'NOUN':
            word = token.text.lower()
            parsed_word = pymorph.parse(word)[0].normal_form
            words.append(parsed_word)

    return " ".join(words)
