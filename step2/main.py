from selenium import webdriver

SIMILAR_ACCOUNT = "chefsteps"
USERNAME = ""
PASSWORD = ""

class InstaFollowers:
  def __init__(self, path=None):
    self.driver = webdriver.Chrome()

  def login(self):
    pass

  def find_followers(self):
    pass

  def follow(self):
    pass

bot = InstaFollowers()
bot.login()
bot.find_followers()
bot.follow()