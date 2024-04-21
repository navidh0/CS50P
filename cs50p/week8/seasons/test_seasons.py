from seasons import Birth

def test_cal():
    date = Birth("2023-03-05")
    assert date.cal() == "Five hundred twenty-seven thousand forty minutes"
    date = Birth("2022-03-05")
    assert date.cal() == "One million, fifty-two thousand, six hundred forty minutes"
def test_invalid_format():
    try:
        date = Birth("January 1, 1999")
        assert False, "Invalid date"

    except SystemExit:
        pass

