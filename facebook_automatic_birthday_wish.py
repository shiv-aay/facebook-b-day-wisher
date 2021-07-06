from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from getpass import getpass
from time import sleep
import os
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

# Install your browser's driver and put its path in the following line.
driver_address = r"C:\Users\pc\Desktop\chromedriver.exe"
# Here I've used Chrome Browser which is Chromium based.
# hence this script also supports Edge browser with a slight modification

def start(username , password , send_now):
    # incoming notifications during the process causes problems
    # following parameter disables browser notifications
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    # Use following line if you have already have chromedriver and linked it at the top
    # driver=webdriver.Chrome(driver_address , options=chrome_options) # put the path of your driver in the double quotes
    driver = webdriver.Chrome()

    driver.get('https://facebook.com/')
    driver.maximize_window()

    ## Logging in
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID, 'email')))
    username_type = driver.find_element_by_xpath("//input[@name=\"email\"]")
    username_type.send_keys(username)
    password_type = driver.find_element_by_xpath("//input[@name=\"pass\"]")
    password_type.send_keys(password)
    log_in = driver.find_element_by_xpath("//button[@type='submit']")
    log_in.click()
    ## Logged in
    sleep(2)
    ## Going to Birthday's Page
    driver.get('https://facebook.com/events/birthdays/')
    WebDriverWait(driver,100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "._5rpu")))
    try:
        # class 'discj3wi' may change after some time, but class of any element
        # which contains list of all friend's who have birthday today would work
        today = driver.find_elements_by_class_name('discj3wi')
        todays = today[1]

        # inner most div element in form
        wish_forms = todays.find_elements_by_xpath("//div[@data-block='true']")
        names = todays.find_elements_by_tag_name('h2')

        send = False
        if(send_now[0] == 'y' or send_now[0] == 'Y'): send = True

        # names[0] is 'Recent birthdays'
        for wish_form,name in zip(wish_forms,names[1:]):
            try:
                name_of_friend = name.find_element_by_tag_name('span').text.split()[0]
                msg="Happy Birthday " + name_of_friend
                wish_form.find_element_by_tag_name('div').send_keys(msg)
                if(send) : wish_form.send_keys(Keys.ENTER)
            except:
                print("Exception occured for 1 friend")
    except Exception as e:        
            print(str(e))
    input("Close the session?")

# taking inputs
username = input("Enter your facebook email/phone number : ")
send_now = input("Do you want to post wishes instantaneously ? ")
password = getpass()
# start the process
start(username = username , password = password , send_now = send_now)

## For any queries or feedback, feel free to contact me here shivoy4ndixit@gmail.com
