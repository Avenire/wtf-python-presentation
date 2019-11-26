from functools import singledispatch

from nice_handlers.errors import NotFound, BadArgs, VeryBadArgs


@singledispatch
def error_handler(exc):
    return 500


@error_handler.register(VeryBadArgs)
def _(_):
    return 422


@error_handler.register(BadArgs)
def _(_):
    return 400


@error_handler.register(NotFound)
def _(_):
    return 404
