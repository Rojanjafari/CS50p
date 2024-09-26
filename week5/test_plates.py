from plates import is_valid

def test_lenghth():
    assert is_valid('H') == False
    assert is_valid('Cs50') == True

def test_start():
    assert is_valid('C500') == False

def test_firstNum():
    assert is_valid('Cs05') == False

def test_nums():
    assert is_valid('AAA22A') == False

def test_dot():
    assert is_valid('cs.50') == False