import numpy as np
from razdel import sentenize
from navec import Navec
from slovnet import Morph
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.spatial.distance import cosine

import plataurus.constants as constants
from plataurus.utils.processing import process_sentence
from plataurus.utils.variables import get_env_value

NAVEC = Navec.load(get_env_value('NAVEC_ARCHIVE', constants.NAVEC_ARCHIVE))
MORPH = Morph.load(get_env_value('MORPH_ARCHIVE', constants.MORPH_ARCHIVE))
MORPH.navec(NAVEC)


def get_clear_matches(first_text, second_text) -> tuple:
    """

    Parameters
    ----------

    Return
    ------
    """
    first_sentences = list(sentenize(first_text))
    second_sentences = list(sentenize(second_text))

    first_matches = []
    second_matches = []
    for first_sentence in first_sentences:
        for second_sentence in second_sentences:
            if first_sentence.text == second_sentence.text:
                first_matches.append((first_sentence.start, first_sentence.stop))
                second_matches.append((second_sentence.start, second_sentence.stop))

    return tuple(first_matches), tuple(second_matches)


def get_matches(first_text, second_text, threshold=0.6) -> tuple:
    """

    Parameters
    ----------

    Return
    ------
    """
    all_processed_sentences = []
    first_sentences, second_sentences = [], []
    for sentence in sentenize(first_text):
        processed_sentence = process_sentence(MORPH, sentence.text)
        first_sentences.append({"sentence": sentence,
                                "processed_sentence": processed_sentence})
        all_processed_sentences.append(processed_sentence)

    for sentence in sentenize(second_text):
        processed_sentence = process_sentence(MORPH, sentence.text)
        second_sentences.append({"sentence": sentence,
                                "processed_sentence": processed_sentence})
        all_processed_sentences.append(processed_sentence)

    tfidf = TfidfVectorizer()
    tfidf.fit(all_processed_sentences)

    first_matches = []
    second_matches = []
    for first_sentence in first_sentences:
        first_tfidf = tfidf.transform([first_sentence['processed_sentence']]).toarray().ravel()
        if np.all(first_tfidf == 0):
            continue

        for second_sentence in second_sentences:
            second_tfidf = tfidf.transform([second_sentence['processed_sentence']]).toarray().ravel()
            if np.all(second_tfidf == 0):
                continue

            cosine_distance = 1 - cosine(first_tfidf, second_tfidf)
            if cosine_distance >= threshold:
                first_matches.append((first_sentence['sentence'].start, first_sentence['sentence'].stop))
                second_matches.append((second_sentence['sentence'].start, second_sentence['sentence'].stop))

    return tuple(first_matches), tuple(second_matches)

