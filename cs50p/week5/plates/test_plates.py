from plates import is_valid


def test_size():
    assert is_valid('q') == False
    assert is_valid('qw') == True
    assert is_valid('qwertyu')==False
    assert is_valid('qwerty')==True

def test_startText():
    assert is_valid('qw') == True
    assert is_valid('q1') == False
    assert is_valid('qw1')==True
    assert is_valid('q123')==False

def test_numLast():
    assert is_valid('qwe2t') == False
    assert is_valid('qw50') == True
    assert is_valid('qw10ty')==False
    assert is_valid('qwer50')==True

def test_invalidChar():
    assert is_valid('qwert.') == False
    assert is_valid('qwe50!')==False

def test_0start():
    assert is_valid('qw00') == False

