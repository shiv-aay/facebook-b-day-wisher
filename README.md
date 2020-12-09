# Automated Facebook Birthday Wish
This is a simple python script which automatically sends personalized birthday wishes to all your Facebook friends who have birthdays at that day on their timeline.

## Dependencies

This script requires python3 and selenium installed. Download any version of python3 from <a href="https://www.python.org/downloads/">here.</a> For selenium with python installed just run the following code in powershell or in terminal:

```
pip3 install selenium
```

## Setup

Firstly,download this script ie. facebook_automatic_birthday_wish.py file

<i>Note:To use it with firefox change ```driver=webdriver.Edge()``` in line 11 to  ```driver=webdriver.Firefox()``` Then you should download the geckodriver from <a href="https://github.com/mozilla/geckodriver/releases">here.</a>
 Further instructions are given in the script itself as comments
 </i>
 
 After the download you should put the path of the driver in the file like this:
 
 ```
 driver=webdriver.Edge(r"C:\Users\pc\Desktop\msedgedriver.exe")
 ```

After that put your username name and password in the file.

## Run

Just run the script using python in powershell or in terminal like:

```
python3 facebook_automatic_birthday_wish.py
```
