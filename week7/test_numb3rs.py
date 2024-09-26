from numb3rs import validate
import pytest

def test_validate():
    assert validate('255.255.255.255') == True
    assert validate('0.0.0.0') == True
    assert validate('cat') == False
    assert validate('12 125 250 4') == False
    assert validate('1.2.3.1000') == False
    assert validate('...') == False
    assert validate("12.0.") == False 
    assert validate('75.456.76.65') == False