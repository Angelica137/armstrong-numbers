from scripts.armstrongnumber import armstrong_number


def test_armstrong_numner_returns_true():
    assert armstrong_number(9) == True


def test_armstrong_number_returns_false():
    assert armstrong_number(10) == False


def test_armstrong_number_153_true():
    assert armstrong_number(153) == True


def test_armstrong_number_154_false():
    assert armstrong_number(154) == False
