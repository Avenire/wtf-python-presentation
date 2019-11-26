import logging


def bunch_of_nonsense(settings_dict):
    # Some silly code operating on dict-like object protocol. Disregard that.
    key_vals = (f'{key}: {value}' for (key,value) in settings_dict.items())
    logging.debug(
        'Passed settings:\n'
        '\n'.join(key_vals)
    )
    if not 'dark_mode_enabled' in settings_dict:
        return dict()

    is_dark_mode = settings_dict['dark_mode_enabled']

    bg_color = (
        settings_dict.get('dark_mode_bg')
        if is_dark_mode
        else settings_dict.get('light_mode_bg')
    )
    return dict(**settings_dict, current_bg=bg_color)


def set_theme(settings):
    quacks_like_dict = type(settings) is dict
    if not quacks_like_dict:
        raise ValueError('YOU ARE CHEATING, THIS IS NOT DICT!')
    bunch_of_nonsense(settings)

