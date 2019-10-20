list_of_a = ['a']


def test_list_of_a():
    x = list(list_of_a) * 5
    assert x == ['a', 'a', 'a', 'a', 'a']
    x[0] *= 2
    assert x[0] == 'aa'
    assert all(x[0] != other_x for other_x in x[1:])

# This will fail
def test_list_of_list_of_a_incorrect():
    y = [list(list_of_a)] * 5
    y[0] *= 2
    assert y[0] == ['a', 'a']
    assert all(y[0] != other_x for other_x in y[1:])

# This won't
def test_list_of_list_of_a_correct():
    y = [list(list_of_a) for _ in range(5)]
    y[0] *= 2
    assert y[0] == ['a', 'a']
    assert all(y[0] != other_x for other_x in y[1:])



