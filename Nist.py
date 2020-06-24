from selenium import webdriver
from time import sleep
from secrets import username, password


class NistBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('http://202.166.200.102/')

        sleep(2)
        #find login button
        fb_btn = self.driver.find_element_by_xpath('/html/body/header/nav/div/div[1]/span/a')
        fb_btn.click()

        #login
        email_in = self.driver.find_element_by_xpath('//*[@id="username"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="password"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="loginbtn"]')
        login_btn.click()

bot = NistBot()
bot.login()