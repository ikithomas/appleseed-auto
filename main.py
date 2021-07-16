from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def main():
    opts = webdriver.FirefoxOptions()
    opts.add_argument("--headless")
    driver = webdriver.Firefox(options=opts)

    ikithomas(driver)

    driver.close()


# get the definition of docker in ikithomas.com
def ikithomas(driver):
    driver.get("https://www.ikithomas.com")

    link = driver.find_element_by_link_text('Dictionary')
    link.click()

    input_ele = driver.find_element_by_xpath('//*[@id="english-input"]')
    input_ele.send_keys('docker')
    input_ele.send_keys(Keys.ENTER)

    time.sleep(5)

    ele = driver.find_element_by_xpath('//*[@id="english-output"]')

    print(ele.text)


if __name__ == '__main__':
    main()
