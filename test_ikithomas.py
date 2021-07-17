from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class FirefoxDriver:
    def __init__(self):
        opts = webdriver.FirefoxOptions()
        opts.add_argument("--headless")
        self.driver = webdriver.Firefox(options=opts)

    def __enter__(self):
        return self.driver

    def __exit__(self, _type, value, traceback):
        self.driver.close()


def test_ikithomas():
    with FirefoxDriver() as driver:
        driver.get("https://www.ikithomas.com")

        link = driver.find_element_by_link_text('Dictionary')
        link.click()

        input_ele = driver.find_element_by_xpath('//*[@id="english-input"]')
        input_ele.send_keys('docker')
        input_ele.send_keys(Keys.ENTER)

        time.sleep(5)

        ele = driver.find_element_by_xpath('//*[@id="english-output"]')

        assert 'a person who works at a port' in ele.text
