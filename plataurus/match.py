from razdel import sentenize


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
