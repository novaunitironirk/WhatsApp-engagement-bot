from selenium.webdriver.common.by import By
import time

class ChatNavigator:
    def __init__(self, driver):
        self.driver = driver

    def open_chat(self, phone):
        self.driver.get(f"https://web.whatsapp.com/send?phone={phone}")
        time.sleep(5)