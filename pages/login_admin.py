# Author:Yi Sun(Tim) 2024-1-22

'''Login Page'''


class Admin_Portal():
    username_loc = 'xpath=//*[@id="Email"]'
    password_loc = 'xpath=//*[@id="Password"]'
    login_loc = 'xpath=//*[@id="loginForm"]/form/'

    def __init__(self,page):
        self.page = page

    def typeUserName(self,username):
        self.page.fill(self.username_loc,username)

    def typePassword(self,password):
        self.page.fill(self.password_loc,password)

    def clicklogin(self):
        self.page.click(self.login_loc)

    def login(self,username, password):
        self.typeUserName(username)
        self.typePassword(password)
        self.clicklogin()
        self.page.wait_for_load_state("networkidle")

    def getUsername(self):
        username_text = self.page.input_value(self.username_loc)
        print('username is:', username_text)
        return username_text
