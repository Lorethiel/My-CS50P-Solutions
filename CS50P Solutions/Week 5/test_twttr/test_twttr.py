import pytest
from twttr import shorten

def test_novowel():
    assert shorten('Myth') == 'Myth'
    assert shorten('Crypt') == 'Crypt'
    assert shorten('Flysch') == 'Flysch'
    assert shorten('twitter') == 'twttr'
    assert shorten('facebook') == 'fcbk'
    assert shorten('rubberduck') == 'rbbrdck'
    assert shorten('1234') == '1234'
    assert shorten('.,!@?') == '.,!@?'
    assert shorten('Anan') == 'nn'





