from nice_handlers.errors import NotFound, BadArgs


def error_handler(exc):
    if isinstance(exc, NotFound):
        return 404
    elif isinstance(exc, BadArgs):
        return 400
    # todo: add VeryBadArgs handling here!
    else:
        return 500