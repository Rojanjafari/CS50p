from jar import Jar
import pytest

def test_init():
    jar = Jar()

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
    with pytest.raises(ValueError):
        jar.deposit(33)


def test_withdraw():
    jar = Jar()
    jar.deposit(9)
    jar.withdraw(4)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(25)
