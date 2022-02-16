from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from tests.test_reading_and_stepik_ex.conftest import browser


def wait_for_open(browser):
    try:
        WebDriverWait(browser, timeout=5).until(
            lambda x: browser.execute_script('return document.readyState') == 'complete')
        return True
    except TimeoutException:
        return False
