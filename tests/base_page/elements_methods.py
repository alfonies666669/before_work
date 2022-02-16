from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait


def wait(browser, how, what):
    try:
        element = WebDriverWait(browser, 10, ignored_exceptions=
                                                [NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException]
                                ).until(
            EC.presence_of_element_located((how, what))
        )
        return element
    except :
        browser.quit()
        print('\n', how, what, ": ", "Element not found!")
