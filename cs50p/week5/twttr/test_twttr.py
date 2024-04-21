from twttr import shorten


def test_vowels():
    assert shorten('aeiou') == ''
    assert shorten('qwert') == 'qwrt'

def test_numbers():
    assert shorten('cs50') == 'cs50'
    assert shorten('python0') == 'pythn0'

def test_capital():
    assert shorten('AEIOU') == ''
    assert shorten('CODE') == 'CD'

def test_signs():
    assert shorten('!@AEIOU@!') == '!@@!'


