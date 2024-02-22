from asyncio import sleep
import secrets
import string
from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse, cfparse
from pages.login_page import *
import logging
from init_helpers import *
from conftest import *

scenarios('../features/login.feature')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_random_string(length=10):
    characters = string.ascii_lowercase + string.digits
    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    return random_string

@pytest.fixture(scope='function')
def shared_data():
    return {}

@pytest.mark.login
@given("I access the internet web app")
def given_I_access_the_ravs_web_app(navigate_to_internet):
    pass

@then("the login button should be visible")
def then_the_login_button_should_be_visible():
    if check_login_button_exists():
        assert True, "Login button is visible"
    else:
        assert False, "Login button is not visible"

@when('I click on the log in button')
def step_click_login_button():
    click_login_button()

@then('your username is invalid alert should be visible')
def username_is_invalid_visible():
    assert check_username_is_invalid_alert_exists() is True, "Username is invalid alert exists"

@when(cfparse("I provide the {username} and {password}"))
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
        username = generate_random_string(65) + "nhs.net"
        enter_username(username)
        enter_password(password)
    elif "long_password" in password:   
        password = generate_random_string(65)
        enter_username(username)
        enter_password(password)
    elif "valid" in username.lower() and "invalid" not in username.lower():
        username = username.strip("-valid")
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
    click_login_button()

@then(parse("login should succeed - {status}"))
@then("login should succeed - <status>")
def verify_signin_status(status, shared_data):
    data = shared_data
    if status.lower() == "fail":
        if data['password'] == "None" and "valid" not in data["username"].lower():
            assert check_password_is_invalid_alert_exists()
            assert get_invalid_error_text() == "\n            Your password is invalid!\n            ×\n          "
        elif data['username'] == "None" and "valid" not in data["username"].lower():
            assert check_username_is_invalid_alert_exists() 
            assert get_invalid_error_text() == "\n            Your username is invalid!\n            ×\n          "      
        elif "long_username" in data['username']:
            assert check_username_is_invalid_alert_exists()   
            assert get_invalid_error_text() == "\n            Your username is invalid!\n            ×\n          "      
        elif "valid" in data['username'] and status.lower()=="pass":
            assert check_logout_button_exists() 
            click_logout_button()
        else:
            assert check_username_is_invalid_alert_exists()