from um import count

def test_count():
    assert count('instrumental') == 0
    assert count('hello') == 0
    assert count('UM, thanks for the album') == 1
    assert count('Um?') == 1