from init_helpers import *

LOGIN_BUTTON_ELEMENT = ("//i[text()=' Login']") 
USERNAME_IS_INVALID_ALERT = ("//div[@class='flash error']")
PASSWORD_IS_INVALID_ALERT = ("//div[@class='flash error']")
USERNAME_INPUT_ELEMENT = ("#username")
PASSWORD_INPUT_ELEMENT = ("#password")


def navigate_to_the_internet_login_page(url):
    navigate_to_url(url)
    wait_for_page_to_load()

def check_login_button_exists():
    wait_for_page_to_load()
    return check_element_exists(LOGIN_BUTTON_ELEMENT, False)

def check_username_is_invalid_alert_exists():
    wait_for_page_to_load()
    return check_element_exists(USERNAME_IS_INVALID_ALERT, False)

def check_password_is_invalid_alert_exists():
    wait_for_page_to_load()
    return check_element_exists(PASSWORD_IS_INVALID_ALERT, False)

def get_invalid_error_text():
    return find_element_and_perform_action(PASSWORD_IS_INVALID_ALERT, "get_text")
    
def click_login_button():
    find_element_and_perform_action(LOGIN_BUTTON_ELEMENT, "click")

def clear_username():
    clear_element(USERNAME_INPUT_ELEMENT)     

def clear_password():
    clear_element(PASSWORD_INPUT_ELEMENT)    

def enter_password(password):
    find_element_and_perform_action(PASSWORD_INPUT_ELEMENT, "input_text", password)        

def enter_username(username):
    find_element_and_perform_action(USERNAME_INPUT_ELEMENT, "input_text", username)            