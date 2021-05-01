import pytest

from owoify.owoify import owoify

source = 'Hello World! This is the string to owo! Kinda cute, isn\'t it?'


def test_owoify():
    assert owoify(source, 'owo') != source


def test_owo():
    assert owoify(source, 'owo') != ''


def test_uwu():
    assert owoify(source, 'uwu') != ''


def test_uvu():
    assert owoify(source, 'uvu') != ''


def test_undefined_level():
    with pytest.raises(RuntimeError):
        owoify(source, '123')


def test_owo_not_equal_to_uwu():
    assert owoify(source, 'owo') != owoify(source, 'uwu')


def test_owo_not_equal_to_uvu():
    assert owoify(source, 'owo') != owoify(source, 'uvu')


def test_uwu_not_equal_to_uvu():
    assert owoify(source, 'uwu') != owoify(source, 'uvu')