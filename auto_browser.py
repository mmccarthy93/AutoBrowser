"""The purpose of this program is to automate the opening and the logging in of multiple websites onto separate tabs
within incognito mode of google chrome."""

import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Set Chrome to open in incognito mode and stay open
chrome_options  = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)

# Open Chrome, navigate to reddit.com, and login
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.reddit.com/login')
time.sleep(1)
reddit_username = browser.find_element_by_id("loginUsername")
reddit_password = browser.find_element_by_id("loginPassword")
  reddit_username.send_keys("USERNAME")
reddit_password.send_keys("PASSWORD")
login_reddit = browser.find_element_by_xpath("//*[@type='submit']")
login_reddit.submit()

# Open gmail in a new tab, login to gmail
window_one = browser.window_handles[0]
browser.execute_script("window.open()")
window_two = browser.window_handles[1]
browser.switch_to.window(window_two)
browser.get('https://www.gmail.com')
time.sleep(1)
gmail_username = browser.find_element_by_id("identifierId")
gmail_username.send_keys("EMAIL ADDRESS")
nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()
browser.implicitly_wait(4)
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
gmail_password = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[1]/div/div[1]/div/div[1]/input")
gmail_password.send_keys("PASSWORD")
nextButton = browser.find_element_by_id('passwordNext')
nextButton.click()

# Open github in new tab, login to github
browser.execute_script("window.open()")
window_three = browser.window_handles[2]
browser.switch_to.window(window_three)
browser.get('https://github.com/login')
time.sleep(1)
github_username = browser.find_element_by_id("login_field")
github_username.send_keys("USERNAME")
github_password = browser.find_element_by_id("password")
github_password.send_keys("PASSWORD")
login_github = browser.find_element_by_xpath("//*[@type='submit']")
login_github.submit()
