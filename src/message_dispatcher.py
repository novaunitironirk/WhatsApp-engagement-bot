import yaml
import random
import time
from chat_navigator import ChatNavigator

class MessageDispatcher:
    def __init__(self, driver):
        self.driver = driver
        self.navigator = ChatNavigator(driver)

    def load_config(self):
        with open("config/campaign.yaml", "r") as f:
            return yaml.safe_load(f)

    def run_campaign(self):
        config = self.load_config()
        contacts = config["campaign"]["contacts"]
        template = config["campaign"]["message_template"]

        for contact in contacts:
            message = template.replace("{{name}}", contact["name"])
            self.navigator.open_chat(contact["phone"])
            self.send_message(message)
            time.sleep(random.randint(5, 8))

    def send_message(self, message):
        from selenium.webdriver.common.by import By
        input_box = self.driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        input_box.send_keys(message)
        input_box.send_keys("\n")