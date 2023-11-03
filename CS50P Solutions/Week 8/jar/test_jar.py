from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.capacity = 15
    with pytest.raises(ValueError):
        assert jar.deposit(20)





def test_withdraw():
    jar = Jar()
    jar.capacity = 15
    with pytest.raises(ValueError):
        assert jar.withdraw(30)
    jar.capacity = 10
    jar.size = 3
    with pytest.raises(ValueError):
        assert jar.withdraw(7)