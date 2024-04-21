from fuel import convert, gauge
import pytest

def test_input():
    assert convert('1/2') == 50
    assert convert('1/1') == 100
    assert convert('0/10') == 0

def test_except():
    with pytest.raises(ZeroDivisionError):
         convert('1/0')
    with pytest.raises(ValueError):
         convert('2/1')

def test_output():
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(50) == '50%'
