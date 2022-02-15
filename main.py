import json
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium import webdriver

browser = webdriver.Chrome()


def get_article():
    link = 'https://en.wikipedia.org/wiki/Main_Page'
    try:
        browser.get(link)
        time.sleep(3)
        option0 = browser.find_element(By.XPATH, "//li[@id='n-randompage']")
        option0.click()
        time.sleep(1)
        main_title = browser.find_element(By.XPATH, '//h1[@id="firstHeading"]')
        text_title = main_title.text
        when_title = browser.find_element(By.XPATH, "//li[@id='footer-info-lastmod']")
        text_footer = when_title.text
        main_text = browser.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/p[2]")
        text_main = main_text.text
        example = {
            "title": text_title,
            "main_text": text_main,
            "when": text_footer
        }
        time.sleep(1)
        with open("title_list.json", "w") as file:
            json.dump(example, file, indent=4)
        browser.quit()
        browser.close()
    except Exception as ex:
        browser.quit()
        browser.close()


get_article()
