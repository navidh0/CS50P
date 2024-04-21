from numb3rs import validate

def test_char():
    assert validate('127.0.0.1') == True
    assert validate('....') == False
    assert validate('!.!.!.!') == False
def test_range():
    assert validate('0.0.0.0') == True
    assert validate('256.256.256.256') == False
    assert validate('8.256.8.8') == False
    assert validate('8.97.101.222') == True
def test_alpha():
    assert validate('8.8.8.8') == True
    assert validate('google.0.0.1') == False
    assert validate('8.google.0.1') == False
    assert validate('8.0.google.1') == False
    assert validate('8.0.0.google') == False
def test_len():
    assert validate('1.2.3.4') == True
    assert validate('1.2.3') == False
    assert validate('1.2') == False
    assert validate('1') == False
