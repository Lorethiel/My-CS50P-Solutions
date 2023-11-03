import pytest
from numb3rs import validate

def test_true():
    assert validate('127.0.0.1') == True
    assert validate('0.0.0.0') == True
    assert validate('255.255.255.255') == True

def test_short():
    assert validate('0.0.0') == False

def test_long():
    assert validate('1.1.1.1.1') == False

def test_bigsmall():
    assert validate('256.257.258.999') == False
    assert validate('-1.-2.-3.-4') == False

def test_string():
    assert validate("bee.2.3.4") == False
    assert validate("1.boo.1.1") == False
    assert validate("1.2.budger.4") == False
    assert validate("1.1.1.baa") == False
    assert validate("zoo") == False

#tests for regex version

def test_regex():
    assert validate(r'1.1.1.1') == True
    assert validate(r'1.2.3') == False
    assert validate(r'1.2') == False
    assert validate(r'1') == False
    assert validate(r'255.311.255.255') == True
    assert validate(r'512.1.1.1') == False
    assert validate(r'1.312.1.1') == False
    assert validate(r'1.1.512.1') == False
    assert validate(r'1.1.1.444') == False