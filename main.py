from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

with open("data.json", "w") as f:
    json.dump([], f)


# function to add to JSON
def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)


browser = webdriver.Chrome()
browser.get(
    'https://www.amazon.com/s?i=fashion-mens&bbn=23610284011&rh=n%3A7141123011%2Cn%3A23610284011%2Cn%3A7147441011%2Cn%3A2474937011%2Cn%3A7072330011&s=date-desc-rank&pd_rd_r=e5e1857c-bbfe-45d6-af23-5b27ae9ad438&pd_rd_w=nkD8L&pd_rd_wg=ZoTze&pf_rd_p=41ae5658-451a-4892-b55b-ce7f394a9f2c&pf_rd_r=QHGY715PAXZZ4WTV3EAG&qid=1659977415&ref=sr_pg_1')

isNextDisabled = False

while not isNextDisabled:
    try:
        element = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-component-type="s-search-result"]')))

        elem_list = browser.find_element(By.CSS_SELECTOR,
                                         "#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.sg-row > div.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div")

        items = elem_list.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

        # print(len(item))

        for item in items:
            title = item.find_element(By.TAG_NAME, 'h5').text
            price = "Bedone Gheymat"

            try:
                price = item.find_element(By.CSS_SELECTOR, '.a-price').text.replace("\n", ".")
            except:
                pass

            print("Title: " + title)
            print("Gheymat: " + price + "\n")

            write_json({
                'title': title,
                'gheymat': price,
            })

        next_btn = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, 's-pagination-next')))

        next_class = next_btn.get_attribute('class')

        if "disabled" in next_class:
            isNextDisabled = True
        else:
            browser.find_element(By.CLASS_NAME, 's-pagination-next').click()

    except Exception as e:
        print(e, "Error dar inja")
        isNextDisabled = True
