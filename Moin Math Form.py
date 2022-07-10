from selenium import webdriver
from time import sleep
from random import *
from faker import Faker

fake = Faker("en_IN")
count = 0
loop_till = 50
#Repeat the process 120 times!!

driver = webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfsw_XJVOoFRzmJYehTFm3HpW_x5zKzmuGH_jPi4V9EX5paxQ/viewform?usp=sf_link")

while(count<loop_till):
    sleep(6)
    name_field = driver.find_element_by_xpath('//input[@aria-labelledby="i1"]')
    name_field.click()
    sleep(2)
    name = fake.unique.name()
    name_field.send_keys(name)
    sleep(2)

    gender_div = ['i9', 'i12']
    rand_gender_div = gender_div[randint(0,1)]
    gender= driver.find_element_by_id("{}".format(rand_gender_div))
    gender.click()
    sleep(2)

    age_field = driver.find_element_by_xpath('//input[@aria-labelledby="i15"]')
    age_field.click()
    sleep(2)
    age = randint(10,20)
    age_field.send_keys(age)
    sleep(2)
    
    height_div = ['i23', 'i26', 'i29', 'i32']
    rand_height_div = height_div[randint(0,3)]
    height= driver.find_element_by_id(f"{rand_height_div}")
    height.click()
    sleep(2)

    weight_field = driver.find_element_by_xpath('//input[@aria-labelledby="i35"]')
    weight_field.click()
    sleep(2)
    weight = randint(30,90)
    weight_field.send_keys(weight)
    sleep(2)
    
    fam_field = driver.find_element_by_xpath('//input[@aria-labelledby="i39"]')
    fam_field.click()
    sleep(2)
    fam = randint(3,10)
    fam_field.send_keys(fam)
    sleep(2)

    mony_div = ['i47', 'i50', 'i53', 'i56', 'i59', 'i62']
    rand_mony_div = mony_div[randint(0,5)]
    mony= driver.find_element_by_id(f"{rand_mony_div}")
    mony.click()
    sleep(2)

    sport_div = ['i69', 'i72', 'i75', 'i78', 'i81']
    rand_sport_div = sport_div[randint(0,4)]
    sport= driver.find_element_by_id(f"{rand_sport_div}")
    sport.click()
    sleep(2)
    sleep(4)

    sn_b = driver.find_element_by_xpath('//div[@jsname="M2UYVd"]')
    sn_b.click()
    sleep(2)

    sleep(2)

    driver.find_element_by_link_text("Submit another response").click()
    sleep(2)
    count+=1

driver.quit()
