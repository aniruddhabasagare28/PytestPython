#Fixtures reusable code comes under fixture
import pytest

@pytest.fixture(scope="module")   #Module, function , class
def preWork():
    print("I setup Module setup")
    return "pass"

@pytest.fixture(scope="function")   #Module, function , class
def second_work():
    print("I setup second_work ")
    yield
    print("I teardown Module setup")

def test_SecondCheck(pre_setup_work):
    print("Initial Check")
