from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class FirefoxDriver:
    def __init__(self):
        opts = webdriver.FirefoxOptions()
        opts.add_argument("--headless")
        self.driver = webdriver.Firefox(options=opts)

    def __enter__(self):
        return self.driver

    def __exit__(self, _type, value, traceback):
        self.driver.close()
