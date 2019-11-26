from assignment.functions_before import (
    increment, make_incrementor, a_getter
)


def test_increment_foo():
    assert a_getter() == 0
    increment()
    assert a_getter() == 1


def test_incrementor():
    incrementor, getter = make_incrementor()
    assert getter() == 0
    assert [incrementor() for _ in range(3)] == [1,2,3]
