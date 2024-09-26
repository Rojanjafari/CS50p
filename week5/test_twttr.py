from twttr import shorten

def test_shortening():
    assert shorten('sAlam.22') == 'slm.22'