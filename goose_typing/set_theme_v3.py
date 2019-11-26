from collections import Mapping

from goose_typing.set_theme_v1 import bunch_of_nonsense


def set_theme(settings):
    # Duck typing is cool but goose typing is cooler B)
    quacks_like_dict = isinstance(settings, Mapping)
    if not quacks_like_dict:
        raise ValueError('YOU ARE CHEATING, THIS IS NOT DICT!')
    bunch_of_nonsense(settings)
