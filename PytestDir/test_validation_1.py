import pytest


def test_test3(prefix_global):
    print('test3 done')


@pytest.mark.smoke
def test_test4(prefix_global):
    print('test4 done')
