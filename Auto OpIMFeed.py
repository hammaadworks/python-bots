from selenium import webdriver
from time import sleep
from random import *

driver = webdriver.Chrome()
driver.get("https://www.infiniquemall.com/infiniquebackend.php")
sleep(4)
#uzer
u=driver.find_element_by_xpath("//input[@id='user_login']")
u.click()
u.send_keys('devteam')
#pazz
p=driver.find_element_by_xpath("//input[@id='user_pass']")
p.click()
p.send_keys('OKQXxI*1!RB^0rze1L8aiAfZ')

driver.find_element_by_xpath("//input[@type='submit']").click()
sleep(2)
driver.find_element_by_xpath("//a[@href='https://www.infiniquemall.com/wp-admin/']").click()
sleep(4)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
sleep(2)

driver.find_element_by_xpath("//img[@src='https://www.infiniquemall.com/wp-content/plugins/wp-product-feed-manager/images/app-rss-plus-xml-icon.png']").click()
sleep(4)

