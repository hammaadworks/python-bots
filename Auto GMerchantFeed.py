from selenium import webdriver
from time import sleep
from random import *

driver = webdriver.Chrome()
driver.get("https://merchants.google.com/mc/products/sources?a=284456364&hl=en&fmp=1&utm_id=gfr&utm_source=google.com&utm_medium=referral&gfr_referral=true&mcsubid=us-en-web-g-mc-gfr")
sleep(4)

driver.find_element_by_xpath("//input[@type='email']").send_keys("myfriendhammad@gmail.com")
# driver.find_element_by_xpath("").click()
# driver.find_element_by_xpath("").send_keys("Hammaad 13")
# driver.find_element_by_xpath("").click()
sleep(4)

