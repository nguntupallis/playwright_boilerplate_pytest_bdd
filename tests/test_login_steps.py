from asyncio import sleep
import secrets
import string
from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse
from pages.login_page import *
import logging
from init_helpers import *
from conftest import *


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_random_string(length=10):
    characters = string.ascii_lowercase + string.digits
    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    return random_string

features_directory = get_working_directory() + "features"

scenarios(f'{features_directory}/login.feature')

@pytest.fixture(scope='function')
def shared_data():
    return {}

@scenario(f'{features_directory}/login.feature', 'Login button is visible')
def test_login_button_is_visible():
    browser_version = get_browser_version()
    allure.dynamic.parameter("Browser Version", browser_version)
    print(f"Browser Version: {browser_version}")
    print("test")

@scenario(f'{features_directory}/login.feature', 'Sign in page should be visible')
def test_sign_in_page_is_visible():
    pass

@scenario(f'{features_directory}/login.feature', 'Sign in should pass or fail based on credentials provided')
def test_sign_in_should_status():
    pass

@given("I access the internet web app")
def given_I_access_the_internet_web_app(navigate_to_internet):
    browser_version = get_browser_version()
    allure.dynamic.title("Browser Version" + browser_version)
    print(f"Browser Version: {browser_version}")
    print("test")

@then("the login button should be visible")
def then_the_login_button_should_be_visible():
    if check_login_button_exists():
        attach_screenshot("expected_login_button_is_visible.png")
        assert True, "Login button is visible"        
    else:
        attach_screenshot("expected_login_button_is_not_visible.png")
        assert False, "Login button is not visible"

@when('I click on the log in button')
def step_click_login_button():
    attach_screenshot("before_the_login_button_is_clicked.png")
    click_login_button()

@then('your username is invalid alert should be visible')
def username_is_invalid_visible():
    assert check_username_is_invalid_alert_exists() is True, "Username is invalid alert exists"

@when(parse("I provide the {username} and {password}"))
@when("I provide the <username> and <password>")
def provide_credentials(username, password, shared_data):
    if username == "None":
        clear_username()
        clear_password()
        enter_password(password)
    elif password == "None":
        clear_password()
        clear_username()
        enter_username(username)
    elif "long_username" in username:   
        username = generate_random_string(65) + ".net"
        enter_username(username)
        enter_password(password)
    elif "long_password" in password:   
        password = generate_random_string(65)
        enter_username(username)
        enter_password(password)
    elif "valid" in username.lower() and "invalid" not in username.lower():
        username = username.strip("_valid")
        enter_username(username)
        password=config["credentials"]["password"]
        if password == "":
            assert False, "Please provide password as environment variable"
        enter_password(password)    
    else:
        enter_username(username)
        enter_password(password)        
    shared_data['username'] = username
    shared_data['password'] = password        

@when("the login button is clicked")
def click_login():
    attach_screenshot("before_the_login_button_is_clicked.png")
    click_login_button()

@then(parse("login should succeed - {status}"))
@then("login should succeed - <status>")
def verify_signin_status(status, shared_data):
    attach_screenshot("the_login_button_is_clicked.png")
    data = shared_data
    if status.lower() == "fail":
        if data['password'] == "None" and "valid" not in data["username"].lower():
            assert check_password_is_invalid_alert_exists() is True
            assert get_invalid_error_text() == "\n            Your password is invalid!\n            ×\n          "
        elif data['username'] == "None" and "valid" not in data["username"].lower():
            assert check_username_is_invalid_alert_exists() is True
            assert get_invalid_error_text() == "\n            Your username is invalid!\n            ×\n          "      
        elif "long_username" in data['username']:
            assert check_username_is_invalid_alert_exists() is True
            assert get_invalid_error_text() == "\n            Your username is invalid!\n            ×\n          "      
    elif status.lower()=="pass":
        assert check_logout_button_exists() == True
        click_logout_button()
    else:
        assert check_username_is_invalid_alert_exists() is True