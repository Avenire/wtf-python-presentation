from default_args.doge import BadDoge, GoodDoge


def test_good_doge_keeps_track_of_his_own_food():
    doge = GoodDoge()
    doge.feed('food')
    assert doge._food != GoodDoge.__init__.__defaults__[0]


def test_bad_doge_binds_to_static_defaults():
    doge = BadDoge()
    doge.feed('food')
    assert doge._food == BadDoge.__init__.__defaults__[0]
    assert id(doge._food) == id(BadDoge.__init__.__defaults__[0])
