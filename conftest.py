import pytest

@pytest.fixture(scope="session",autouse=True)
def setUp():
    print("open amazon app")
    print("user loged in")
    yield
    print("loged out")
    print("closed amazon")
