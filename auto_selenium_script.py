from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Set up Selenium webdriver (ensure you have chromedriver installed and in your PATH)
driver = webdriver.Chrome(options=chrome_options)

driver.get(f"https://app.vodex.ai")
time.sleep(3)

for i in 