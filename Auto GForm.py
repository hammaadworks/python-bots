from selenium import webdriver
from time import sleep
from random import *
from faker import Faker

fake = Faker("en_IN")
count = 0
loop = 1
#Repeat the process 120 times!!

driver = webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdL6LYus3_Vicd4zFuaEd_WrTLtdTUTrbMYnlfzjFh9TbKuIw/viewform")

while(count<loop):
    sleep(6)
    name_field = driver.find_element_by_xpath('//input[@aria-labelledby="i3"]')
    name_field.click()
    sleep(2)
    name = fake.unique.name()
    name_field.send_keys(name)

    sleep(2)

    age_div = ['i11', 'i14', 'i17', 'i20', 'i23']
    rand_age_div = age_div[randint(0,4)]
    age= driver.find_element_by_id("{}".format(rand_age_div))
    age.click()
    sleep(2)
            
    gender_div = ['i30', 'i33']
    rand_gender_div = gender_div[randint(0,1)]
    gender= driver.find_element_by_id("{}".format(rand_gender_div))
    gender.click()
    sleep(2)

    aware_div = ['i46', 'i49', 'i52']
    rand_aware_div = aware_div[randint(0,2)]
    aware = driver.find_element_by_id("{}".format(rand_aware_div))
    aware.click()
    sleep(2)

    info_div = ['i59', 'i62', 'i65']
    rand_info_div = info_div[randint(0,2)]
    info= driver.find_element_by_id("{}".format(rand_info_div))
    info.click()
    sleep(2)

    comfy_div = ['i72', 'i75', 'i78']
    rand_comfy_div = comfy_div[randint(0,2)]
    comfy= driver.find_element_by_id("{}".format(rand_comfy_div))
    comfy.click()
    sleep(2)

    no_div = ['i85', 'i88', 'i91', 'i94']
    rand_no_div = no_div[randint(0,3)]
    no= driver.find_element_by_id("{}".format(rand_no_div))
    no.click()
    sleep(2)

    yes_div = ['i101', 'i104', 'i107', 'i110']
    rand_yes_div = yes_div[randint(0,3)]
    yes= driver.find_element_by_id("{}".format(rand_yes_div))
    yes.click()
    sleep(2)

    bank_div = ['i117', 'i120', 'i123', 'i126', 'i129', 'i132', 'i135']
    rand_bank_div = bank_div[randint(0,6)]
    bank= driver.find_element_by_id("{}".format(rand_bank_div))
    bank.click()
    sleep(2)

    pref_div = ['i142', 'i145', 'i148', 'i151', 'i154']
    rand_pref_div = pref_div[randint(0,4)]
    pref= driver.find_element_by_id("{}".format(rand_pref_div))
    pref.click()
    sleep(2)

    demo_div = ['i161', 'i164', 'i167', 'i170']
    rand_demo_div = demo_div[randint(0,3)]
    demo= driver.find_element_by_id("{}".format(rand_demo_div))
    demo.click()
    sleep(2)

    rur_div = ['i177', 'i180', 'i183']
    rand_rur_div = rur_div[randint(0,2)]
    rur= driver.find_element_by_id("{}".format(rand_rur_div))
    rur.click()
    sleep(2)

    pur_div = ['i190', 'i193', 'i196', 'i199']
    rand_pur_div = pur_div[randint(0,3)]
    pur= driver.find_element_by_id("{}".format(rand_pur_div))
    pur.click()
    sleep(2)

    mid_div = ['i206', 'i209', 'i212']
    rand_mid_div = mid_div[randint(0,2)]
    mid= driver.find_element_by_id("{}".format(rand_mid_div))
    mid.click()
    sleep(2)

    tim_div = ['i219', 'i222', 'i225', 'i228']
    rand_tim_div = tim_div[randint(0,3)]
    tim= driver.find_element_by_id("{}".format(rand_tim_div))
    tim.click()
    sleep(2)
    
    
    opt = randint(1,10)
    lev = driver.find_element_by_xpath('//div[@data-value="{}"]'.format(opt))
    lev.click()
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
