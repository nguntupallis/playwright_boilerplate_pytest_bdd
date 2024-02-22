from init_helpers import *

LOGOUT_BUTTON_ELEMENT = ("//i[text()=' Logout']") 

def check_logout_button_exists_without_waiting():
    return check_element_exists(LOGOUT_BUTTON_ELEMENT, False)

def check_logout_button_exists():
    return check_element_exists(LOGOUT_BUTTON_ELEMENT, True)
    
def click_logout_button():
    find_element_and_perform_action(LOGOUT_BUTTON_ELEMENT, "click")    