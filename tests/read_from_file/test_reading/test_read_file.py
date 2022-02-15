from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.read_from_file.read import reading
from selenium.webdriver.chrome.options import Options
import time
import math
import pytest

final = ''


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    chrome_options = Options()
    chrome_options.add_argument('headless')
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    print("\nquit browser..")
    time.sleep(5)
    browser.quit()
    print(final)


def test_read():
    test_data = ["one\n", "two\n", "three"]
    with open("ttestread.txt", "a") as fil:
        fil.writelines(test_data)
    assert test_data == reading("ttestread.txt")


def test_read2():
    test_data = ["one\n", "two\n", "three"]
    with open("ttestread.txt", "a") as fil:
        fil.writelines(test_data)
    assert test_data == reading("ttestread.txt")


@pytest.mark.parametrize('url', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_parametrize(browser, url):
    global final
    link = f'https://stepik.org/lesson/{url}/step/1'
    browser.get(link)
    browser.implicitly_wait(10)
    option0 = browser.find_element(By.CSS_SELECTOR, "textarea")
    option0.send_keys(str(math.log(int(time.time()))))
    button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    button.click()
    x_element = browser.find_element(By.CSS_SELECTOR, "pre.smart-hints__hint").text
    if x_element != "Correct!":
        final += x_element
    assert 'Correct!' == x_element
