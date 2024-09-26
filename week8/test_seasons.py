from seasons import check_date, age_calculator, convertor
import pytest

def test_check_date():
    with pytest.raises(SystemExit):
        check_date('1999/08/01')
    with pytest.raises(SystemExit):
        check_date('1999-8-1')
    with pytest.raises(SystemExit):
        check_date('February 6th, 1998')
    assert check_date('2004-06-06') == '2004-06-06'

def test_age_calculator():
    assert age_calculator('2023-08-08') == 527040

def test_convertor():
    assert convertor(527040) == 'Five hundred twenty-seven thousand forty minutes'