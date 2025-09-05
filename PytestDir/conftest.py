import pytest


@pytest.fixture(scope='module')
def prefix_global():
    print('browser initialization via conftest')