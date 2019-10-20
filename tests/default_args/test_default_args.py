from tests.default_args.doge import BadDoge as Doge


def test_doge_remembers_food_it_was_fed():
    doge = Doge()
    doge.feed('chicken')
    assert doge._food == ['chicken']


def test_doge_remembers_food_it_was_fed_if_doge_was_feed_before():
    doge_that_ate_before = Doge(food=['beef'])
    doge_that_ate_before.feed('salad')
    assert doge_that_ate_before._food == ['beef', 'salad']


def test_doge_remembers_food_it_was_feed_if_doge_is_vege():
    vege_doge = Doge()
    vege_doge.feed('carrot')
    assert vege_doge._food == ['carrot']
