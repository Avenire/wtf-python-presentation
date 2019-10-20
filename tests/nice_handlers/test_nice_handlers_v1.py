from unittest.mock import MagicMock

import pytest

from tests.nice_handlers.error_handlers_v1 import error_handler
from tests.nice_handlers.errors import NotFound, BadArgs, VeryBadArgs
from tests.nice_handlers.view import some_view


@pytest.mark.parametrize(
    'exception, expected', [
        (NotFound, 404),
        (BadArgs, 400),
        (ValueError, 500),
        (VeryBadArgs, 422)
    ])
def test_handles_errors(exception, expected):
    code = some_view(
        some_service=MagicMock(side_effect=exception),
        error_handler=error_handler
    )
    assert code == expected

