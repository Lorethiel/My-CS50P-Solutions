import pytest
from bank import value


def test_bank():
    assert value('Hello') == 0
    assert value('hello') == 0
    assert value('hey') == 20
    assert value('zarto') == 100
    assert value('h') == 20
    assert value('HELLO') == 0
