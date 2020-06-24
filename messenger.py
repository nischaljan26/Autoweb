from selenium import webdriver
from time import sleep
from secrets import muser, mpword


class MessengerBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        # self.driver.get('https://fb.com/')
        self.driver.get('https://m.me/')

        sleep(2)
        #login
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(muser)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(mpword)

        login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_btn.click()

bot = MessengerBot()
bot.login()