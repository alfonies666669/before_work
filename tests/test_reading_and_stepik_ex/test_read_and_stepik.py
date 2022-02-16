import math
import time
import pytest
from selenium.webdriver.common.by import By
from tests.test_reading_and_stepik_ex.read import reading
from tests.base_page.page_methods import *
from tests.base_page.elements_methods import *

final = ''


@pytest.mark.skip()
def test_read():
    test_data = ["one\n", "two\n", "three"]
    with open("ttestread.txt", "a") as fil:
        fil.writelines(test_data)
    assert test_data == reading("ttestread.txt")


@pytest.mark.skip()
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
    if wait_for_open(browser):
        try:
            option0 = wait(browser, By.XPATH, "//textarea[@class]")
            option0.send_keys(str(math.log(int(time.time()))))
            button = wait(browser, By.XPATH, "//button[@class = 'submit-submission']")
            button.click()
            x_element = wait(browser, By.XPATH, "//pre[@class='smart-hints__hint']").text
            if x_element != "Correct!":
                final += x_element
            assert 'Correct!' == x_element
            with open("text_on_the_field.txt", "w") as file:
                file.write(final)
            with open("text_on_the_field.txt", "r") as fil:
                text_on_file = fil.readline()
                print(text_on_file)
        except:
            print("test failed")
