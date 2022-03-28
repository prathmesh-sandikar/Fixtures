import pytest


@pytest.fixture()
def setUp():
    print("setup started")
    yield
    print("exited")
def test_AddItemtoCart(setUp):
    print("Added successfully")


def test_RemoveItemFromCart(setUp):
    print("Removed successfully")