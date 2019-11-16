import pytest
from selenium import webdriver

from POM.login import Login


@pytest.mark.usefixtures("onetimeSetup","setup")
class TestCalssDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.log_in=Login()
        print("class label setup of pypi org")
        yield
        print("logging out of py pi")

        def test_tc123_verify_login(self):

            assert self.log_in.login_to_account()
            assert self.log_in.verify_login()
