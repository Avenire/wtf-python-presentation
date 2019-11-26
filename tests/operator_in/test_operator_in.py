import pytest

from tests.operator_in.utils import secret_decorator


def test_obvious_fail_case():
    """
    Plain classes can't use `in` operator. Note the error "is not *iterable*".
    :return:
    """
    class NotComptaibleWithInOperator:
        pass

    with pytest.raises(
        TypeError,
        match=(
            'TypeError: argument of type '
            '\'NotComptaibleWithInOperator\' is not iterable'
        )
    ):
        'some_key' in NotComptaibleWithInOperator()


def test_implements_with_contains():
    """
    Normally we'd implement this by overriding dunder-contains-dunder method.
    """
    class CompatibleWithContains:
        def __contains__(self, item):
            return False

    assert not 'some_key' in CompatibleWithContains()


def test_implements_with_iterable():
    """
    What if we try with iterable class.
    """
    class CompatibleWithContains:
        def __iter__(self):
            return iter(())

    assert not 'some_key' in CompatibleWithContains()


def test_implements_with_other_iterable():
    """
    We can also...
    """
    class CompatibleWithContains:
        def __iter__(self):
            yield

    assert not 'some_key' in CompatibleWithContains()


# Don't check implementation before first run unless you can tell what's
# wrong with the test :)!
@secret_decorator
def test_iterable_madness():
    """
    Tip: Debug this test if you've no idea what's going on.
    :return:
    """
    class SillyClass:
        def __getitem__(self, item):
            return None
    instance = SillyClass()
    assert instance['s'] is instance[0] is None
    assert not 's' in instance


def test_iterable_madness_vol_2():
    """
    ***
    DO NOT READ BEFORE YOU UNDERSTAND TEST ABOVE! :)
    ***
    ░░░░░░░░▄▄▄▀▀▀▄▄███▄░░░░░░░░░░░░░░
    ░░░░░▄▀▀░░░░░░░▐░▀██▌░░░░░░░░░░░░░
    ░░░▄▀░░░░▄▄███░▌▀▀░▀█░░░░░░░░░░░░░
    ░░▄█░░▄▀▀▒▒▒▒▒▄▐░░░░█▌░░░░░░░░░░░░
    ░▐█▀▄▀▄▄▄▄▀▀▀▀▌░░░░░▐█▄░░░░░░░░░░░
    ░▌▄▄▀▀░░░░░░░░▌░░░░▄███████▄░░░░░░
    ░░░░░░░░░░░░░▐░░░░▐███████████▄░░░
    ░░░░░le░░░░░░░▐░░░░▐█████████████▄
    ░░░░toucan░░░░░░▀▄░░░▐█████████████▄
    ░░░░░░has░░░░░░░░▀▄▄███████████████
    ░░░░░arrived░░░░░░░░░░░░█▀██████░░
    It seems if you implement __getitem__ then Python assumes you might be iterable as well!
    And `in` operator sort-of-works. Python checks if our class hides items
    we look for by testing integer-indices. And it does for eternity. Sooooo
    to stop this all we need to do is implement __len__ right...
    """
    class SillyClassV2:
        def __getitem__(self, item):
            return None

        def __len__(self):
            return 0
    instance = SillyClassV2()
    assert not 's' in instance


def test_iterable_madness_vol_3():
    """
    ...well, nope. This time Python doesn't try to be clever. We need to
    raise `IndexError`.
    """
    class SillyClassV3:
        def __getitem__(self, item):
            if item > 5:
                raise IndexError()
            return None

    instance = SillyClassV3()
    assert not 's' in instance
