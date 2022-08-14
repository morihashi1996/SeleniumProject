import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://turbolearn.ir/accounts/login/?next=/profile/')

cookies = pickle.load(open("cookies.pkl", "rb"))

for cookie in cookies:
    cookie['domain'] = ".turbolearn.ir"

    try:
        browser.add_cookie(cookie)
    except Exception as e:
        print(e)

browser.get('https://turbolearn.ir/profile/')

time.sleep(50)
