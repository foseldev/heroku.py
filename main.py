import streamlit as st

#st.title("ff")

from selenium.webdriver.chrome.options import Options
########################################################
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')
#########################################################

            
#########################################################
try:
    browser = webdriver.Chrome('C:/Users/Water/Desktop/chromedriver.exe', options=options) # Chrome Driver
    browser.get('https://www.wholefoodsmarket.com/products/all-products?featured=on-sale') # Website Link
    print('Enter the zipcode of your local WholeFoods...')
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("zipcode")
        args = parser.parse_args()
        zipcode = str(args.zipcode)
        browser.find_element_by_xpath("//input[@id='pie-store-finder-modal-search-field']").send_keys(zipcode) # Zip code
    except:
        browser.find_element_by_xpath("//input[@id='pie-store-finder-modal-search-field']").send_keys(input()) # Zip code
