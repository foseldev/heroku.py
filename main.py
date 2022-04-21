import streamlit as st

#st.title("ff")

print('ñ')


from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.google.com")
print('El texto es:')
time.sleep(1)
driver.find_element_by_xpath("//div[contains(text(),'Acepto')]").click()
print('si')
st.title("ff")
driver.quit()
