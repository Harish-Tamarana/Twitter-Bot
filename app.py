from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Twitterbot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(3)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def likeTweet(self, hashtag):
        bot = self.bot
        time.sleep(3)
        bot.get('https://twitter.com/search?q=' + hashtag + '&src=typd')
        for i in range(1, 4):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
            tweets = bot.find_elements_by_css_selector('[data-testid="tweet"]')
            links = [elem.get_attribute('data-permalink-path')
                     for elem in tweets]
            print(links)



harry = Twitterbot('your_profile_name', 'Your_password') # Make sure to enter your twitter username and password correctly 

harry.login()
harry.likeTweet('anime')
