from selenium.webdriver.common.by import By

from src.common.selenium_wrapper import SeleniumWrapper


class TestDemo:
    def test_demo(self):
        driver = SeleniumWrapper()
        driver.open_url("https://www.google.com/")
        search_input = driver.find_element((By.NAME, "q"))
        search_input.send_keys("iphone 15 pro max")
        search_input.submit()
        print("Title: ", driver.get_title())
        print("URL: ", driver.get_current_url())

