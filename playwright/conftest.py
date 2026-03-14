import pytest


@pytest.fixture(scope="session")   #Module, function , calss
def user_credentials(request):
    return request.param
