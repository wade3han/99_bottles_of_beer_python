import pytest

from bottles import Bottles


@pytest.fixture(scope="module")
def bottles() -> Bottles:
    return Bottles()
