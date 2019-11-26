from goose_typing.set_theme_v1 import set_theme


# It starts easy...
def test_succeeds_for_dict():
    settings = {'dark_mode_enabled': True, 'dark_mode_bg': '#000000',
                'light_mode_bg': '#FFFFFF'}
    assert set_theme(settings)


# ...but then people want to use OrderedDicts too...
def test_succeeds_for_ordered_dict_too():
    from collections import OrderedDict
    settings = OrderedDict(
        {'dark_mode_enabled': True, 'dark_mode_bg': '#000000',
         'light_mode_bg': '#FFFFFF'}
    )
    assert set_theme(settings)


# ...then some Python 2 weirdo comes in...
def test_succeeds_for_user_dict_as_well():
    from collections import UserDict
    settings = UserDict(
        {'dark_mode_enabled': True, 'dark_mode_bg': '#000000',
         'light_mode_bg': '#FFFFFF'}
    )
    assert set_theme(settings)



