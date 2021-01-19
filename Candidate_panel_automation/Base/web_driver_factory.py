from selenium import webdriver
import os
import time
import pytest

class WebDriverFactory:
    def __init__(self, browser):
        self.browser= browser

    def get_web_driver_instance(self):
        baseURL = "https://profiledev.workex.ai/auth/login"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            chromedriver = "/home/kavya/tools/chromedriver_linux64/chromedriver"
            os.environ["webdriver.chrome"] = chromedriver
            driver = webdriver.Chrome(chromedriver)


        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        time.sleep(2)
        driver.get(baseURL)
        time.sleep(4)

        # Maximize the window
        driver.maximize_window()

        # Loading browser with App URL

        return driver