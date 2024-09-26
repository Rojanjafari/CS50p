from fuel import gauge, convert
import pytest

def test_convert():
    assert convert('99/100') == 99
    with pytest.raises(ZeroDivisionError):
        assert convert('0/0')
    with pytest.raises(ValueError):
        assert convert('4/3')
    with pytest.raises(ValueError):
        assert convert('three/four')

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(75) == '75%'
