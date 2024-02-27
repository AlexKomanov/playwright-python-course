import pytest


def test_one_add_one():
    assert 1 + 1 == 2


def test_one_add_two():
    num_1 = 1
    num_2 = 2
    result = 3
    print(f"{result = }")
    assert num_1 + num_2 == result, "A result should be three"


def test_divide_by_zero():
    with pytest.raises(Exception) as err:
        num_1 = 5 / 0

    assert str(err.value) == 'division by zero'
    assert err.type == ZeroDivisionError


# Parametrized Test -> Don't Repeat Yourself
test_data = [
    (2, 3, 6),
    (99, 1, 99),
    (0, 10, 0),
    (-5, 1, -5),
    (-5, -2, 10),
]


@pytest.mark.parametrize("num_1, num_2, result", test_data)
def test_multiplication(num_1, num_2, result):
    assert num_1 * num_2 == result

