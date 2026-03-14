import pytest


@pytest.fixture(scope="session")   #Module, function , calss
def pre_setup_work():
    print("I setup browser")
