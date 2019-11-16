import pytest
from selenium import webdriver

@pytest.yield_fixture()

def setup():
    print("Running method")
    yield
    print("running teardown method")

@pytest.yield_fixture(scope="class")
def oneTimeSetup(browser):
    print("Running one time setup")
    if browser=="firefox":
        print("running in FF")
    else:
        print("running in chrome")
    yield
    print("running one time teardown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def broswer(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):

    return request.config.getoption("--osType")

