from source.accum import Accumulator
import pytest


# @pytest.fixture
# def accum():
#     return Accumulator(3)


@pytest.fixture
def accum2():
    return Accumulator()


def test_new_accum(accum_global, accum2):
    assert accum_global.count == 0
    assert accum2.count == 0


@pytest.mark.sanity
def test_add_counts(accum):
    accum.add_counts()
    assert accum.count == 1


@pytest.mark.sanity
def test_add_counts_twice(accum):
    accum.add_counts()
    accum.add_counts()
    assert accum.count == 2


@pytest.mark.regression
def test_add_counts_with_params(accum):
    accum.add_counts(10)
    assert accum.count == 10


def test_add_counts_and_setter(accum):
    accum.count = 2
    accum.add_counts()
    assert accum.count == 3


def test_get_brand(accum):
    with pytest.raises(AttributeError) as err:
        print(accum.__brand)

    assert str(err.value) == "'Accumulator' object has no attribute '__brand'"
