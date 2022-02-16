import pytest
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def clean_text_file():
    with open('ttestread.txt', "w") as file:
        pass


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    chrome_options = Options()
    chrome_options.add_argument('headless')
    #chrome_options.add_argument('--start-maximized')
    browser = webdriver.WebDriver(options=chrome_options)
    yield browser
    print("\nquit browser..")
    browser.quit()
