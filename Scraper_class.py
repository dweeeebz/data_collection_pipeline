from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://zoopla.co.uk")



driver.find_element(by=By.XPATH, value='//button')