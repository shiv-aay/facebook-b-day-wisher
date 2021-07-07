# Automated Facebook Birthday Wish
This is a simple python script which automatically sends personalized birthday wishes to all your Facebook friends who have birthdays at that day on their timeline.

NOTE : This script is originally built for Chrome browser on windows OS. With slight modifications, it can be easily used on different browsers or OS.

This script can be directly installed with a single command
```
pip install fbwisher
```
Run the script by typing `fbwisher` in the terminal.

Cheers!

**Alternatively**

Clone this repo using 
```
git clone https://github.com/shiv-aay/facebook-b-day-wisher
```
Go to that directory
```
cd facebook-b-day-wisher
```

## Dependencies

This script requires python3 and selenium installed. Download any version of python3 from <a href="https://www.python.org/downloads/">here.</a> For selenium with python installed just run the following code in powershell or in terminal:

```
pip install -r requirements.txt
```

## Setup for other broswers

<i>Note:To use it with firefox use ```driver=webdriver.Firefox()``` Then you should download the geckodriver from <a href="https://github.com/mozilla/geckodriver/releases">here.</a>
 Further instructions are given in the script itself as comments
 </i>
Similar instructions to be followed for Edge.

## Run

Just run the script using python in powershell or in terminal like:

```
python facebook_automatic_birthday_wish.py
```
Enter login credentials, password(unechoed) once

In case, you want to reset your credentials or choices, just delete `credentials.txt` file inside the cloned folder.
