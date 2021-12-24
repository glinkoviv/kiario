from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://www.kia.ru/personal/")
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".nav-tabs__item:nth-child(2)")))
    button = browser.find_element_by_css_selector(".nav-tabs__item:nth-child(2)")
    button.click()
    browser.implicitly_wait(1)
    body = browser.find_element_by_tag_name("body")
    body.send_keys(Keys.TAB)
    input1 = browser.find_element_by_css_selector("li:nth-child(1) input")
    input1.send_keys("+79102625505")
    body = browser.find_element_by_tag_name("body")
    body.send_keys(Keys.TAB)
    input2 = browser.find_element_by_css_selector("li:nth-child(2) input")
    input2.send_keys("Frog")
    body.send_keys(Keys.TAB)
    input3 = browser.find_element_by_css_selector("li:nth-child(3) input")
    input3.send_keys("Pepe")
    body.send_keys(Keys.TAB)
    input4 = browser.find_element_by_css_selector("li:nth-child(4) input")
    input4.send_keys("frogpepe@gmail.com")
    body.send_keys(Keys.TAB)
    click = browser.find_element_by_css_selector("li:nth-child(5) label")
    browser.execute_script("window.scrollTo(0, window.scrollY + 400)")
    click.click()
    body.send_keys(Keys.TAB)
    body.send_keys(Keys.TAB)
    click2 = browser.find_element_by_css_selector("li:nth-child(6) label")
    click2.click()
    browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
    click3 = browser.find_element_by_class_name("button_primary")
    click3.click()
    body.send_keys(Keys.TAB)
    body.send_keys(Keys.ENTER)
finally:
    time.sleep(20)
    browser.quit()