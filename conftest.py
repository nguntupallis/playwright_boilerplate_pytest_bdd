import logging
import pytest
from pages.login_page import *
from pages.home_page import *
from init_helpers import *
from datetime import datetime, timedelta
import allure
from allure_commons._core import plugin_manager
from allure_pytest.listener import AllureListener
from allure_commons.types import LabelType

logging.basicConfig(level=logging.INFO)

pytest.mark.login = pytest.mark.mark(login=True)
pytest.mark.logout = pytest.mark.mark(logout=True)

pytest.mark.login
@pytest.fixture(scope='function')
def navigate_and_login(request, navigate_to_internet):
    click_login_button()
    username = "tomsmith"
    enter_username(username)
    password = config["credentials"]["password"]
    enter_password(password)
    click_login_button()

@pytest.fixture(scope='module', autouse=True)
def report_browser_version(request):
    browser_version = get_browser_version()
    allure.dynamic.label(LabelType.TAG, browser_version)
    logging.info(config["browser"].upper() + f" browser version is : {browser_version}")

pytest.mark.login
@pytest.fixture(scope='function')
def navigate_to_internet(request):
    if check_logout_button_exists_without_waiting():
        click_logout_button()
    url = get_app_url(config["test_environment"])
    navigate_to_the_internet_login_page(url)
    return True