from owoify.utility.interleave_arrays import interleave_arrays
from owoify.utility.presets import *
from owoify.structures.word import Word
import re


WORD_REGEX = re.compile(r'[^\s]+')
SPACE_REGEX = re.compile(r'\s+')


def map_owoify_levels(word: Word, level: str) -> Word:
    """
    Utility function to map different level of owoness to the string.
    For internal use only.
    :exception RuntimeError: When the inputted owoness level is incorrect.
    :param word: The source Word to owoify.
    :param level: The desired owoness level.
    :return: The owoified Word.
    """
    level = level.lower()
    for func in SPECIFIC_WORD_MAPPING_LIST:
        word = func(word)
    if level == 'owo':
        for func in OWO_MAPPING_LIST:
            word = func(word)
    elif level == 'uwu':
        for func in UWU_MAPPING_LIST:
            word = func(word)
        for func in OWO_MAPPING_LIST:
            word = func(word)
    elif level == 'uvu':
        for func in UVU_MAPPING_LIST:
            word = func(word)
        for func in UWU_MAPPING_LIST:
            word = func(word)
        for func in OWO_MAPPING_LIST:
            word = func(word)
    else:
        raise RuntimeError('The specified owoify level is not supported.')
    return word


def owoify(source: str, level: str = 'owo') -> str:
    """
    The main entry point of owoify. Pass the source string and the desired level of owoness to owoify it.
    :exception RuntimeError: When the inputted owoness level is incorrect.
    :param source: The source string to owoify.
    :param level: The owoness to apply to the string. Available options are: `owo`, `uwu`, `uvu` (from low to high).
    :return: The owoified string.
    """
    word_matches = WORD_REGEX.findall(source)
    space_matches = SPACE_REGEX.findall(source)

    words = [Word(s) for s in word_matches]
    spaces = [Word(s) for s in space_matches]

    words = list(map(lambda w: map_owoify_levels(w, level), words))

    result = interleave_arrays(words, spaces)
    result_strings = list(map(lambda w: str(w), result))
    return ''.join(result_strings)
