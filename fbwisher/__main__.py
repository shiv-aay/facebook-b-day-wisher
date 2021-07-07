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
    driver = webdriver.Chrome(options=chrome_options)

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
    sleep(1)
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
    input("Close the session? ")

def main():
    # taking inputs
    if os.path.exists("credentials.txt"):
        lines = []
        with open('credentials.txt') as f:
            lines = f.readlines()
        username = lines[0].rstrip()
        send_now = lines[1].rstrip()
        password = lines[2].rstrip()
        start(username = username , password = password , send_now = send_now)
    else:
        print("Hi there! Welcome to Facebook Birthday Post Automation Script. Let's get started by setting up your chrome driver...\n")
        chromedriver_autoinstaller.install()
        print("Chrome Driver Set. \n\nGet your seat belts on and be ready for a quick ride. \nBut first, let's answer some difficult questions\n")

        print("# NOTE : The following questions will be asked, only the first time you use this script on your device")
        print("If you want to reset this information, delete `credentials.txt` file inside the folder. And needless to say, don't worry about your privacy. This is a completely safe and open-souce script. \nCheers!\n")    
        username = input("Enter your facebook email/phone number : ")
        send_now = input("Do you want to post wishes instantaneously ? ")
        password = getpass("Enter your facebook password (unechoed) : ")
        file = open("credentials.txt","a")
        lines = [username, send_now, password]
        for line in lines:
            file.write(line + "\n")
        file.close()
        # start the process
        start(username = username , password = password , send_now = send_now)

if __name__ == "__main__" : main()
## For any queries or feedback, feel free to contact me here shivoy4ndixit@gmail.com
