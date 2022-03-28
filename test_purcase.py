import pytest


@pytest.fixture()
def setUp():
    print("user loged in")
    yield
    print("loged out")
def test_AddItemtoCart(setUp):
    print("Added successfully")


def test_RemoveItemFromCart(setUp):
    print("Removed successfully")