from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class igbot:

    def __init__(self, headless, gecko_path=None):
        if headless is True:
            self.options = Options()
            self.options.headless = True
            self.login_status = False
            self.notification_status = None
            if gecko_path is None:
                self.browser = webdriver.Firefox(options=self.options)
            else:
                self.browser = webdriver.Firefox(options=self.options,
                                                 executable_path=r'{path}'.format(path=gecko_path))
        else:
            self.login_status = False
            self.notification_status = None
            if gecko_path is None:
                self.browser = webdriver.Firefox()
            else:
                self.browser = webdriver.Firefox(executable_path=r'{path}'.format(path=gecko_path))

    def login(self, username, password):
        self.browser.implicitly_wait(5)
        self.browser.get('https://www.instagram.com/')
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(5)
        try:
            if self.browser.find_element_by_xpath("//a[@href='/{username}/']".format(username=username)):
                self.login_status = self.login_confirmation(username)
                print("Logged In!")
            else:
                self.login_status = False
                print("Failed to login!")
        except:
            self.login_status = False
            print("Failed to login!")

    def login_confirmation(self, username):
        self.browser.get('https://www.instagram.com/{usrname}/'.format(usrname=username))
        sleep(5)
        try:
            if self.browser.find_element_by_xpath("//button[text()='Edit Profile']"):
                return True
            else:
                return False
        except:
            return False

    def open_inbox(self):
        if self.login_status is True:
            self.browser.get('https://www.instagram.com/direct/inbox/')
            try:
                if self.browser.find_element_by_xpath("//div[text()='Direct']"):
                    print("Opened Inbox")
                    return True
                else:
                    print("Could not Open Inbox")
                    return False
            except:
                print("Could not Open Inbox")
                return False
        else:
            print("Your Are not Logged In!")

    def turn_on_notification_state(self):
        if self.login_status is True:
            try:
                if self.browser.find_element_by_xpath("//button[text()='Turn On']"):
                    try:
                        if self.browser.find_element_by_xpath("//button[text()='Not Now']"):
                            return True
                    except:
                        return False
            except:
                return False
        else:
            print("Your Are not Logged In!")

    def turn_on_notification_action(self, value):
        if self.login_status is True:
            if self.turn_on_notification_state() is True:
                if value is True:
                    turn_on_notification = self.browser.find_element_by_xpath("//button[text()='Turn On']")
                    turn_on_notification.click()
                    self.notification_status = True
                    print('Disabled Notification Popup!')
                else:
                    turn_off_notification = self.browser.find_element_by_xpath("//button[text()='Not Now']")
                    turn_off_notification.click()
                    self.notification_status = False
                    print('Disabled Notification Popup!')
            else:
                print("Notification Popup Not Detected!")
        else:
            print("Your Are not Logged In!")

    def open_inbox(self):
        if self.login_status is True:
            self.browser.get('https://www.instagram.com/direct/inbox/')
            try:
                if self.browser.find_element_by_xpath("//div[text()='Direct']"):
                    print("Opened Inbox")
                    return True
                else:
                    print("Could not Open Inbox")
                    return False
            except:
                print("Could not Open Inbox")
                return False
        else:
            print("Your Are not Logged In!")

    def pre_checklist(self):
        if self.login_status is True:
            sleep(5)
            inbox_status = self.open_inbox()
            if inbox_status is True:
                self.turn_on_notification_action(False)
                if self.notification_status is False:
                    print("Pre-Check Done!")
                elif self.notification_status is True:
                    print("Pre-Check Done!")
            else:
                print("Pre-Check Failed!")
        else:
            print("Your Are not Logged In!")

    def chat_search_opener(self):
        if self.login_status is True:
            state = self.open_inbox()
            if state is True:
                try:
                    search_button = self.browser.find_element_by_xpath("//button[@class='wpO6b ZQScA']")
                    search_button.click()
                    return True
                except:
                    return False
            else:
                return False
        else:
            print("Your Are not Logged In!")

    def chat_search_and_open(self, username):
        if self.login_status is True:
            try:
                state = self.chat_search_opener()
                if state is True:
                    seach_input = self.browser.find_element_by_xpath("//input[@placeholder='Search...']")
                    seach_input.send_keys(username)
                    sleep(5)
                    seach_result = self.browser.find_element_by_xpath(
                        "//div[@class='                    Igw0E   rBNOH        eGOV_    "
                        " ybXk5    _4EzTm                                                "
                        "                                   XfCBB          HVWg4         "
                        "        ']")
                    seach_result.click()
                    next_button = self.browser.find_element_by_xpath("//button[text()='Next']")
                    next_button.click()
                    return True
            except:
                return False
        else:
            print("Your Are not Logged In!")

    def send_dm(self, username, message):
        if self.login_status is True:
            state = self.chat_search_and_open(username)
            if state is True:
                type_message = self.browser.find_element_by_xpath("//textarea[@placeholder='Message...']")
                type_message.send_keys(message)
                send_button = self.browser.find_element_by_xpath("//button[text()='Send']")
                send_button.click()
                print("DM Sent!")
            else:
                print("An Error Occoured sending DM")
        else:
            print("Your Are not Logged In!")
