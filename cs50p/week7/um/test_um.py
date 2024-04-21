from um import count



def test_word():
    assert count('um') == 1
    assert count('um?') == 1
    assert count('album') == 0
    assert count('yummy') == 0
def test_string():
    assert count('hello, um, world') == 1
    assert count('um, thanks for the album') == 1
def test_ignorecase():
    assert count('UM') == 1
    assert count('Um, thanks for the album') == 1
