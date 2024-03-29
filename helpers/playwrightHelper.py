from collections import defaultdict
from playwright.sync_api import sync_playwright
from axe_core_python.sync_playwright import Axe
from init_helpers import *

class ElementNotFoundException(Exception):
    pass

class BasePlaywrightHelper:
    def __init__(self, working_directory, config):
        playwright_instance = sync_playwright().start()
        self.working_directory = working_directory
        self.screenshots_dir = "screenshots"
        if not os.path.exists(self.screenshots_dir):
            os.makedirs(self.screenshots_dir)
        self.playwright = playwright_instance
        self.browser = None
        self.context = None
        self.page = None
        self.browser_versions = defaultdict(str)
       
    def launch_chromium(self, headless_mode):
        try:
            self.browser = self.playwright.chromium.launch(headless=headless_mode)
            self.context = self.browser.new_context()
            self.page = self.context.new_page()
        except Exception as e:
            print(f"Error launching Chromium: {e}")

    def launch_edge(self, headless_mode):
        try:
            self.browser = self.playwright.chromium.launch(channel="msedge",headless=headless_mode)
            self.context = self.browser.new_context()
            self.page = self.context.new_page()
        except Exception as e:
                print(f"Error launching Edge: {e}")

    def launch_safari(self, headless_mode):
        try:
            self.browser = self.playwright.webkit.launch(headless=headless_mode)
            self.context = self.browser.new_context()
            self.page = self.context.new_page()
        except Exception as e:
                print(f"Error launching Edge: {e}")

    def launch_chrome(self, headless_mode):
        try:
            self.browser = self.playwright.chromium.launch(channel="chrome", headless=headless_mode)
            self.context = self.browser.new_context()
            self.page = self.context.new_page()
        except Exception as e:
            print(f"Error launching Safari: {e}")

    def launch_firefox(self, headless_mode):
        try:
            self.browser = self.playwright.firefox.launch(headless=headless_mode)
            self.page = self.browser.new_page()
            self.context = self.browser.new_context()
        except Exception as e:
            print(f"Error launching Firefox: {e}")

    def launch_mobile_browser(self, device_name, headless_mode):
        ua_string_android_chrome = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.40 Mobile Safari/537.36'
        ua_string_android_samsung_internet = 'Mozilla/5.0 (Linux; Android 13; K; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/24.0 Chrome/117.0.0.0 Mobile Safari/537.36'
        ua_string_iphone_safari = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Mobile/15E148 Safari/604.1'
        ua_string_iphone_chrome = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.6312.52 Mobile/15E148 Safari/604.1'
        
        try:
            if "iphone_12" == device_name.lower():
                self.browser = self.playwright.webkit.launch(headless=headless_mode)
                self.context = self.browser.new_context(**self.playwright.devices["iPhone 12"])
            elif "iphone_11" == device_name.lower():
                self.browser = self.playwright.chromium.launch(channel="chrome", headless=headless_mode)
                self.context = self.browser.new_context(**self.playwright.devices["iPhone 11"])
            elif "pixel_5" == device_name.lower():
                self.browser = self.playwright.webkit.launch(headless=headless_mode)
                self.context = self.browser.new_context(**self.playwright.devices["Pixel 5"])
            else:
                self.browser = self.playwright.chromium.launch(channel='chromium', headless=headless_mode)
                self.context = self.browser.new_context(**self.playwright.devices["Galaxy S9+"])

            self.page = self.context.new_page()
        except Exception as e:
            print(f"Error launching mobile browser for {device_name}: {e}")

    def capture_screenshot(self, filename):
        screenshot_path = os.path.join(self.screenshots_dir, f'before_action_{filename}.png')
        self.page.screenshot(path=screenshot_path)
        return screenshot_path

    def get_browser_version(self):
        if self.browser:
            print(self.browser.version)
            return self.browser.version
        else:
            return None

    def close_browser(self):
        if self.context:
            self.context.close()             
        if self.browser:
            self.browser.close()            

    def navigate_to_url(self,url):
        print(f"Navigating to URL: {url}")
        self.page.goto(url)

    def wait_for_page_to_load(self, timeout=10):
        self.page.wait_for_load_state('domcontentloaded', timeout=timeout * 1000)

    def check_element_exists(self, selector, wait=False):
        self.wait_for_page_to_load()        
        try:
            element = self.page.locator(selector)
            if wait == True:
                self.page.wait_for_selector(selector)
            return element.is_visible()
        except Exception as e:
            print(f"Element not found: {e}")
            return False
        
    def clear_element(self, selector):
        self.wait_for_page_to_load()
        try:
            element=self.page.locator(selector)
            element.clear()
            print(f"Cleared text from the {selector} successfully.")
        except Exception as e: 
            print(f"Exception: {e}. Element not found.")
            raise ElementNotFoundException(f"Element not found: {selector}")
        
    def find_element_and_perform_action(self, selector, action, inputValue=None):
        self.wait_for_page_to_load()
        selector_filename = "".join(c if c.isalnum() else "_" for c in selector)
        before_screenshot_path = os.path.join(self.screenshots_dir, f'before_action_{selector_filename}.png')
        self.page.screenshot(path=before_screenshot_path)
        try:
            self.page.wait_for_selector(selector)
            element=self.page.locator(selector)
            if action.lower() == "click":
                element.click()
                print(f"Clicked the {selector} successfully.")
            elif action.lower() == "input_text":
                text = element.text_content()
                if text != '':
                    element.clear()
                element.fill(inputValue)
                print(f"Entered text into the {selector} successfully.")
            elif action.lower() == "get_text":
                text = element.text_content()
                print(f"Text from the {selector}: {text}")
                return text
            elif action.lower() == "select_option":
                element.select_option(inputValue)
                print(f"Selected option with value '{inputValue}' from the {selector} successfully.")
            elif action.lower() == "click_checkbox":
                if not element.is_checked():
                    element.check()
                    print(f"{selector} checkbox checked successfully.")
                else:
                    print(f"{selector} checkbox is already checked.")
            else:
                print(f"Unsupported action: {action}")
        except Exception as e:
            print(f"Exception: {e}. Element not found: {selector}")
            raise ElementNotFoundException(f"Element not found: {selector}")
        after_screenshot_path = os.path.join(self.screenshots_dir, f'after_action_{selector_filename}.png')
        self.page.screenshot(path=after_screenshot_path)

    def get_current_url(self):
        self.wait_for_page_to_load()
        return self.page.url()

    def get_accessibility_violations(self):
        try:
            current_url = self.get_current_url(self.page)

            self.page.goto(current_url)
            self.wait_for_page_to_load(self.page)

            axe = self.page.accessibility
            results = axe.check()
            violations = results['violations']

            if violations:
                print(f"Accessibility Violations for {current_url}: {violations}")
            else:
                print(f"No accessibility violations found for {current_url}.")

            return violations

        except Exception as e:
            print(f"Exception during accessibility testing: {e}")
            return None

    def quit_browser(self):
        try:
            if self.page:
                self.page.close()
            if self.browser:
                self.browser.close()
            if self.playwright:
                self.playwright.stop()
        except Exception as e:
            print(f"An error occurred during browser cleanup: {e}")                     

class PlaywrightHelper(BasePlaywrightHelper):
    def __init__(self, working_directory, config):
        super().__init__(working_directory, config)
        
        try:
            browser_name = config["browser"].lower()
            headless_mode = config["headless_mode"].lower() == "true"
            if browser_name == "chromium":
                self.launch_chromium(headless_mode)
            if browser_name == "chrome":
                self.launch_chrome(headless_mode)
            elif browser_name == "firefox":
                self.launch_firefox(headless_mode)
            elif browser_name == "safari":
                self.launch_safari(headless_mode)
            elif "edge" in browser_name:
                self.launch_edge(headless_mode)
            elif browser_name == "mobile":
                self.launch_mobile_browser(config["device"], headless_mode)
            else:
                print(f"Unsupported browser: {browser_name}")
        except Exception as e:
            print(f"Error launching browser: {e}")        
