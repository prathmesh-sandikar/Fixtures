import pytest
@pytest.fixture()
def setUp():
    print("open amazon app")
    print("user loged in")
    yield
    print("loged out")
    print("closed amazon")




def test_checkout(setUp):
    print("payment successfully")