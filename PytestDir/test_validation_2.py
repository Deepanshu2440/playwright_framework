import pytest


# //fixtures
# - something which we will use everytime like browser initiate or login
# it is passed as argument to the test__ fn
# @pytest.fixture(scope='module') or @pytest.fixture(scope='function')
# here function execute for all fn and in module it is execuited once for all tests

# function - every time
# module - once per file
# session - once per whole execution
# YIELD : keywords used to pause the flow in fixture and once fn executes the conditoon after yeild is executed

@pytest.fixture(scope='function')
def prefix():
    print('browser initialization')
    return 'pass'


@pytest.fixture(scope='function')
def prefix_suffix():
    print('browser initialization inside yield usage fn')
    yield
    print('closing browser')


@pytest.mark.smoke
@pytest.mark.skip
def test_test1(prefix,prefix_suffix):
    print('test1 done')
    assert prefix == 'pass'


def test_test2(prefix):
    print('test2 done')
