from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep

# Install your browser's driver and put its path in the following line. 
# Here I've used Edge Browser which is Chromium based, Chromium can also be used here
## https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
driver=webdriver.Edge(r"C:\Users\pc\Desktop\msedgedriver.exe") # put the path of your driver in the double quotes
driver.get('https://facebook.com/')
driver.maximize_window()

## Logging in
WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID, 'email')))
username_type = driver.find_element_by_xpath("//input[@name=\"email\"]")
username_type.send_keys("example@gmail.com")#Enter your username in double quotes
password_type = driver.find_element_by_xpath("//input[@name=\"pass\"]")
password_type.send_keys("example_password")#Enter your password in double quotes
log_in = driver.find_element_by_xpath("//button[@type='submit']")
log_in.click()
## Logged in
sleep(2)
## Going to Birthday's Page
driver.get('https://facebook.com/events/birthdays/')
WebDriverWait(driver,100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "._5rpu")))
try:
    todays = driver.find_element_by_class_name('sjgh65i0')
    wish_forms = todays.find_elements_by_class_name('_5rpu')
    # todays = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]")
    # wish_forms = todays.find_elements_by_xpath("/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/form/div/div/div[1]/div/div/div[2]/div")
    names = todays.find_elements_by_class_name('cbu4d94t')
    for wish_form,name in zip(wish_forms,names[1:]):
        msg="Happy Birthday "+name.text.split()[0]
        wish_form.send_keys(msg)
        # Uncomment the next line to automatically send the wishes
        ## wish_form.send_keys(Keys.ENTER)
except Exception as e:
        print(str(e))

## For any queries or feedback, feel free to contact me here shivoydixit@outlook.com