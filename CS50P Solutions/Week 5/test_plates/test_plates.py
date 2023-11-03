import pytest
from plates import is_valid


def test_twotwo():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False

def test_smashedn():
    assert is_valid('CS50P') == False


def test_unknown():
    assert is_valid('PI3.14') == False

def test_short():
    assert is_valid('H') == False
    assert is_valid('AA') == True
    assert is_valid('A2') == False
    assert is_valid('2A') == False
    assert is_valid('22') == False
    assert is_valid(' 2') == False

def test_long():
    assert is_valid('OUTATIME') == False

