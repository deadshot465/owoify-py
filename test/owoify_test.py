import pytest

from owoify.owoify import owoify, Owoness

source = 'Hello World! This is the string to owo! Kinda cute, isn\'t it?'
pokemon_name_list_path = 'assets/pokemons.txt'
war_and_peace_path = 'assets/war_and_peace_chapter01-20.txt'

with open(pokemon_name_list_path) as file:
    pokemon_names = file.readlines()

with open(war_and_peace_path) as file:
    war_and_peace_text = file.read()


def test_owoify():
    assert owoify(source) != source


def test_owo():
    text = owoify(source, Owoness.Owo)
    assert text != ''
    assert text is not None


def test_uwu():
    text = owoify(source, Owoness.Uwu)
    assert text != ''
    assert text is not None


def test_uvu():
    text = owoify(source, Owoness.Uvu)
    assert text != ''
    assert text is not None


def test_undefined_level():
    with pytest.raises(RuntimeError):
        owoify(source, 3)


def test_owo_not_equal_to_uwu():
    assert owoify(source, Owoness.Owo) != owoify(source, Owoness.Uwu)


def test_owo_not_equal_to_uvu():
    assert owoify(source, Owoness.Owo) != owoify(source, Owoness.Uvu)


def test_uwu_not_equal_to_uvu():
    assert owoify(source, Owoness.Uwu) != owoify(source, Owoness.Uvu)


def test_pokemon_names():
    for name in pokemon_names:
        name_with_owo = owoify(name)
        name_with_uwu = owoify(name, Owoness.Uwu)
        name_with_uvu = owoify(name, Owoness.Uvu)
        assert name_with_owo != ''
        assert name_with_uwu != ''
        assert name_with_uvu != ''
        assert name_with_owo is not None
        assert name_with_uwu is not None
        assert name_with_uvu is not None


def test_long_text():
    text_with_owo = owoify(war_and_peace_text)
    text_with_uwu = owoify(war_and_peace_text, Owoness.Uwu)
    text_with_uvu = owoify(war_and_peace_text, Owoness.Uvu)
    assert text_with_owo != ''
    assert text_with_uwu != ''
    assert text_with_uvu != ''
    assert text_with_owo is not None
    assert text_with_uwu is not None
    assert text_with_uvu is not None
