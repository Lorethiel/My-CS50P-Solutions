from fuel import gauge,convert
import pytest

def test_vlzr():
    with pytest.raises(ValueError):
        convert('x/y')
    with pytest.raises(ZeroDivisionError):
        convert('7/0')

def test_convert():
    assert convert('1/2') == 50
    assert convert("0/1") == 0
    assert convert('1/4') == 25
    assert convert('1/1') == 100

def test_gauge():
    assert gauge(75) == '75%'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'