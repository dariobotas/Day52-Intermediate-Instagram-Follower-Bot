import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SIMILAR_ACCOUNT = "chefsteps"
USERNAME = ""
PASSWORD = ""


class InstaFollowers:
    def __init__(self, path=None):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login")
        time.sleep(5)

        username = self.driver.find_element(By.NAME, value="username")
        password = self.driver.find_element(By.NAME, value="password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        pass

    def follow(self):
        pass


bot = InstaFollowers()
bot.login()
bot.find_followers()
bot.follow()
