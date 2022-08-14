import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from password import pass2, em

email = em
password = pass2

browser = webdriver.Chrome()
browser.get('https://turbolearn.ir/accounts/login/?next=/profile/')

browser.find_element(By.ID, 'id_email').send_keys(email)
password_selector = "#id_password"
WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, password_selector)))
browser.find_element(By.CSS_SELECTOR, password_selector).send_keys(password)

browser.find_element(By.XPATH, '//*[@id="login"]/div/div/div/div/div/form/button').click()

time.sleep(5)

cookies = browser.get_cookies()

pickle.dump(cookies, open("cookies.pkl", "wb"))
