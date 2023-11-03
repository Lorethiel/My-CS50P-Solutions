from um import count
import pytest



def test_um1():
    assert count('um') == 1

def test_um2():
    assert count('um, um, yummy') == 2


def test_um3():
    assert count('Um, im giving you a gift.') == 1
    assert count('hello, world') == 0