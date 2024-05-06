from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class SeleniumWrapper:
    def __init__(self, browser="chrome", headless=False, disable_args=None):
        if browser.lower() == "chrome":
            chrome_options = ChromeOptions()
            if headless:
                chrome_options.add_argument("--headless")
            if disable_args:
                for arg in disable_args:
                    chrome_options.add_argument(f"--disable-{arg}")
            self.driver = webdriver.Chrome(options=chrome_options)

    def open_url(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    def maximize_window(self):
        self.driver.maximize_window()

    def find_element(self, locator=None, parent=None, timeout=10):
        if parent:
            return WebDriverWait(parent, timeout).until(EC.presence_of_element_located(locator))
        else:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator, parent=None, timeout=10):
        element = self.find_element(locator, parent, timeout)
        element.click()

    def input_text(self, locator, text, parent=None, timeout=10):
        element = self.find_element(locator, parent, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, parent=None, timeout=10):
        element = self.find_element(locator, parent, timeout)
        return element.text

    def click_button(self, locator, parent=None, timeout=10):
        self.click_element(locator, parent, timeout)

    def select_checkbox(self, locator, parent=None, timeout=10):
        checkbox = self.find_element(locator, parent, timeout)
        if not checkbox.is_selected():
            checkbox.click()

    def deselect_checkbox(self, locator, parent=None, timeout=10):
        checkbox = self.find_element(locator, parent, timeout)
        if checkbox.is_selected():
            checkbox.click()

    def select_radio_button(self, locator, parent=None, timeout=10):
        self.click_element(locator, parent, timeout)

    def select_dropdown_option_by_value(self, locator, value, parent=None, timeout=10):
        element = self.find_element(locator, parent, timeout)
        select = Select(element)
        select.select_by_value(value)

    def select_dropdown_option_by_index(self, locator, index, parent=None, timeout=10):
        element = self.find_element(locator, parent, timeout)
        select = Select(element)
        select.select_by_index(index)

    def select_dropdown_option_by_visible_text(self, locator, text, parent=None, timeout=10):
        element = self.find_element(locator, parent, timeout)
        select = Select(element)
        select.select_by_visible_text(text)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    def get_all_window_handles(self):
        return self.driver.window_handles

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def get_alert_text(self):
        return self.driver.switch_to.alert.text
