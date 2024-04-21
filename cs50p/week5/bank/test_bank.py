from bank import value


def test_hello():
    assert value('hello') == 0
    assert value('hello, Newman') == 0


def test_h():
    assert value('how you doing') == 20
    assert value('hey') == 20


def test_nonH():
    assert value('whats up') == 100


def test_capital():
    assert value('HELLO') == 0
    assert value('HEY') == 20
    assert value('Whats up') == 100
