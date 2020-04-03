import random_name


def test_two_name():
    result = random_name.random_two_name()
    assert len(result) == 2


def test_three_name():
    result = random_name.random_three_name()
    result_s = random_name.random_three_names()
    assert len(result) == 3
    assert len(result_s) == 3


def test_four_name():
    result = random_name.random_four_name()
    assert len(result) == 4


def test_chinese_name():
    result = random_name.random_chinese_name()
    assert 1 < len(result) < 5
