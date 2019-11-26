from goose_typing.set_theme_v1 import bunch_of_nonsense


def set_theme(settings):
    # Let's try again.
    quacks_like_dict = isinstance(settings, dict)
    if not quacks_like_dict:
        raise ValueError('YOU ARE CHEATING, THIS IS NOT DICT!')
    bunch_of_nonsense(settings)
