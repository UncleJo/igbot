from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()
login_status = False
username = ""
password = ""
credential_status = False


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
    if browser.find_element_by_xpath("//button[text()='Edit Profile']"):
        return True
    else:
        return False


def set_credentials():
    global username, password, credential_status, login_status
    username = str(input("username - "))
    password = str(input("password - "))
    credential_status = True
    login_status = login(username, password)
    if login_status is True:
        print("Logged In!")
        menu()
    else:
        print("Wrong Credentials, Enter Again")
        set_credentials()


def menu():
    print(0)


def main():
    global credential_status, login_status
    if credential_status is False:
        print("Enter credentials")
        set_credentials()
    else:
        login_status = loginconfirmation(username)
        if login_status is True:
            print("Logged In!")
            menu()
        else:
            print("Wrong Credentials, Enter Again")
            set_credentials()


main()