def foo(a, *b, c=None):
    return True


def other_foo(a, *, c=None):
    return True


def test_stars():
    assert foo(1,2)
    assert other_foo(1,2)
