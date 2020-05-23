from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()
login_status = False
username = ""
password = ""
credential_status = False
turn_on_notification_status = None


def login(username, password):
    browser.implicitly_wait(5)
    browser.get('https://www.instagram.com/')
    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")
    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    sleep(5)
    if browser.find_element_by_xpath("//a[@href='/{username}/']".format(username=username)):
        confirmation = loginconfirmation(username)
    else:
        confirmation = False
    if confirmation is True:
        return True
    else:
        return False


def loginconfirmation(username):
    browser.get('https://www.instagram.com/{usrname}/'.format(usrname=username))
    sleep(5)
    if browser.find_element_by_xpath("//button[text()='Edit Profile']"):
        return True
    else:
        return False


def turn_on_notification_state():
    try:
        if browser.find_element_by_xpath("//button[text()='Turn On']"):
            try:
                if browser.find_element_by_xpath("//button[text()='Not Now']"):
                    return True
            except:
                return False
    except:
        return False


def turn_on_notification_action(value):
    global turn_on_notification_status
    if turn_on_notification_state() is True:
        if value is True:
            turn_on_notification = browser.find_element_by_xpath("//button[text()='Turn On']")
            turn_on_notification.click()
        else:
            turn_off_notification = browser.find_element_by_xpath("//button[text()='Not Now']")
            turn_off_notification.click()
            turn_on_notification_status = False
            print('Disabled Notification Popup')
    else:
        print("Not Detected")


def open_inbox():
    browser.get('https://www.instagram.com/direct/inbox/')
    if browser.find_element_by_xpath("//div[text()='Direct']"):
        print("Opened Inbox")
        return True
    else:
        print("Could not Open Inbox")
        return False


def set_credentials():
    global username, password, credential_status, login_status
    username = str(input("username - "))
    password = str(input("password - "))
    credential_status = True
    login_status = login(username, password)
    if login_status is True:
        print("Logged In!")
        checklist()
    else:
        print("Wrong Credentials, Enter Again")
        set_credentials()


def main():
    global credential_status, login_status
    if credential_status is False:
        print("Enter credentials")
        set_credentials()
    else:
        login_status = loginconfirmation(username)
        if login_status is True:
            print("Logged In!")
            checklist()
        else:
            print("Wrong Credentials, Enter Again")
            set_credentials()


def checklist():
    global turn_on_notification_status
    sleep(5)
    inbox_status = open_inbox()
    if inbox_status is True:
        turn_on_notification_action(False)
        if turn_on_notification_status is False:
            print("Pre-Check Done!")
            #onward
    else:
        print("Pre-Check Failed!")


main()
