import pytest


def secret_decorator(func):
    return pytest.mark.timeout(5)(func)
