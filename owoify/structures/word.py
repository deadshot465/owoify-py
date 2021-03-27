from owoify.utility.flatten import flatten
from typing import List, Set, Callable
import re


class Word:
    def __init__(self, word: str):
        self.replaced_words: Set[str] = set()
        self.word = word

    def __str__(self) -> str:
        return self.word

    def selector(self, s: str, search_value: re.Pattern, replace_value: str) -> bool:
        if search_value.search(s) is not None:
            match_result = search_value.search(s).group()
            return s.replace(match_result, replace_value) == replace_value
        return False

    def search_value_contains_replaced_words(self, search_value: re.Pattern, replace_value: str) -> bool:
        return any(self.selector(s, search_value, replace_value) for s in self.replaced_words)

    def replace(self, search_value: re.Pattern, replace_value: str, replace_replaced_words: bool = False):
        if not replace_replaced_words and self.search_value_contains_replaced_words(search_value, replace_value):
            return self
        replacing_word = self.word
        if search_value.search(self.word) is not None:
            replacing_word = search_value.sub(replace_value, self.word)
        collection = search_value.findall(self.word)
        replaced_words: List[str]
        if len(collection) > 1:
            replaced_words = list(map(lambda s: s.replace(s, replace_value), collection))
        else:
            replaced_words = []

        if replacing_word != self.word:
            for word in replaced_words:
                self.replaced_words.add(word)
            self.word = replacing_word
        return self

    def replace_with_func_single(self, search_value: re.Pattern, func: Callable[[], str], replace_replaced_words: bool = False):
        replace_value = func()
        if not replace_replaced_words and self.search_value_contains_replaced_words(search_value, replace_value):
            return self

        replacing_word = self.word
        if search_value.search(self.word) is not None:
            match = search_value.search(self.word).group()
            replacing_word = self.word.replace(match, replace_value)
        collection = search_value.findall(self.word)
        replaced_words: List[str]
        if len(collection) > 1:
            replaced_words = list(map(lambda s: s.replace(s, replace_value), collection))
        else:
            replaced_words = []
        if replacing_word != self.word:
            for word in replaced_words:
                self.replaced_words.add(word)
            self.word = replacing_word
        return self

    def replace_with_func_multiple(self, search_value: re.Pattern, func: Callable[[str, str], str], replace_replaced_words: bool = False):
        if search_value.search(self.word) is None:
            return self
        word = self.word
        captures = search_value.search(word)
        replace_value = func(captures.group(1), captures.group(2))
        if not replace_replaced_words and self.search_value_contains_replaced_words(search_value, replace_value):
            return self
        replacing_word = self.word.replace(captures.group(0), replace_value)
        collection = search_value.findall(self.word)
        collection = list(flatten(collection))
        replaced_words: List[str]
        if len(collection) > 1:
            replaced_words = list(map(lambda s: s.replace(s, replace_value), collection))
        else:
            replaced_words = []

        if replacing_word != self.word:
            for word in replaced_words:
                self.replaced_words.add(word)
            self.word = replacing_word
        return self
