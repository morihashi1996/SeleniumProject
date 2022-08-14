# import undetected_chromedriver as uc
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# email = 'mortezahashmabady@yahoo.com'
# password = 'morteza2121'
#
# browser = webdriver.Chrome()
# browser.get('https://toplearn.com/Login')
#
# browser.find_element(By.ID, 'EmailOrMobilePhone').send_keys(email)
#
# browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/form/div[2]/div[3]/button').click()
#
# password_selector = "#Password"
#
# WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, password_selector)))
#
# browser.find_element(By.CSS_SELECTOR, password_selector).send_keys(password)
#
# browser.find_element(By.CSS_SELECTOR,
#                      'body > div.client-page.register-bg-style > div > div > div > form > div.row > div.col-xs-12 > button').click()
