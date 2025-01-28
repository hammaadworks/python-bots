from selenium import webdriver
from time import sleep
from random import randint
from faker import Faker

# Initialize Faker for generating fake data (Indian locale)
fake = Faker("en_IN")
# Initialize counter for the loop
count = 0
# Set the number of loops to 1 (can be changed for multiple submissions)
loop = 1

# Initialize the Chrome webdriver
driver = webdriver.Chrome()
# Open the Google Form URL in the browser
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdL6LYus3_Vicd4zFuaEd_WrTLtdTUTrbMYnlfzjFh9TbKuIw/viewform")

# Loop to fill and submit the form multiple times (as defined by 'loop')
while count < loop:
    # Wait for 6 seconds to ensure the page is fully loaded
    sleep(6)

    # Find the name field by its XPath
    name_field = driver.find_element_by_xpath('//input[@aria-labelledby="i3"]')
    # Click on the name field to activate it
    name_field.click()
    # Wait for 2 seconds
    sleep(2)
    # Generate a unique fake name
    name = fake.unique.name()
    # Enter the generated name into the name field
    name_field.send_keys(name)

    # Wait for 2 seconds
    sleep(2)

    # List of IDs for age options
    age_div = ['i11', 'i14', 'i17', 'i20', 'i23']
    # Select a random age option from the list
    rand_age_div = age_div[randint(0, 4)]
    # Find the age option element by its ID
    age = driver.find_element_by_id("{}".format(rand_age_div))
    # Click on the selected age option
    age.click()
    # Wait for 2 seconds
    sleep(2)

    # List of IDs for gender options
    gender_div = ['i30', 'i33']
    # Select a random gender option from the list
    rand_gender_div = gender_div[randint(0, 1)]
    # Find the gender option element by its ID
    gender = driver.find_element_by_id("{}".format(rand_gender_div))
    # Click on the selected gender option
    gender.click()
    # Wait for 2 seconds
    sleep(2)

    # List of IDs for awareness options
    aware_div = ['i46', 'i49', 'i52']
    # Select a random awareness option from the list
    rand_aware_div = aware_div[randint(0, 2)]
    # Find the awareness option element by its ID
    aware = driver.find_element_by_id("{}".format(rand_aware_div))
    # Click on the selected awareness option
    aware.click()
    # Wait for 2 seconds
    sleep(2)

    # List of IDs for information options
    info_div = ['i59', 'i62', 'i65']
    # Select a random information option from the list
    rand_info_div = info_div[randint(0, 2)]
    # Find the information option element by its ID
    info = driver.find_element_by_id("{}".format(rand_info_div))
    # Click on the selected information option
    info.click()
    # Wait for 2 seconds
    sleep(2)

    # List of IDs for comfort options
    comfy_div = ['i72', 'i75', 'i78']
    # Select a random comfort option from the list
    rand_comfy_div = comfy_div[randint(0, 2)]
    # Find the comfort option element by its ID
    comfy = driver.find_element_by_id("{}".format(rand_comfy_div))
    # Click on the selected comfort option
    comfy.click()
    # Wait for 2 seconds
    sleep(2)

    # List of IDs for 'no' options
    no_div = ['i85', 'i88', 'i91', 'i94']
    # Select a random 'no' option from the list
    rand_no_div = no_div[randint(0, 3)]
    # Find the 'no' option element by its ID
    no = driver.find_element_by_id("{}".format(rand_no_div))
    # Click on the selected 'no' option
    no.click()
    # Wait for 2 seconds
    sleep(2)

    # List of IDs for 'yes' options
    yes_div = ['i101', 'i104', 'i107', 'i110']
    # Select a random 'yes' option from the list
    rand_yes_div = yes_div[randint(0, 3)]
    # Find the 'yes' option element by its ID
    yes = driver.find_element_by_id("{}".format(rand_yes_div))
    # Click on the selected 'yes' option
    yes.click()
    # Wait for 2 seconds
    sleep(2)

    # List of IDs for bank options
    bank_div = ['i117', 'i120', 'i123', 'i126', 'i129', 'i132', 'i135']
    # Select a random bank option from the list
    rand_bank_div = bank_div[randint(0, 6)]
    # Find the bank option element by its ID
    bank = driver.find_element_by_id("{}".format(rand_bank_div))
    # Click on the selected bank option
    bank.click()
    # Wait for 2 seconds
    sleep(2)

    # List of IDs for preference options
    pref_div = ['i142', 'i145', 'i148', 'i151', 'i154']
    # Select a random preference option from the list
    rand_pref_div = pref_div[randint(0, 4)]
    # Find the preference option element by its ID
    pref = driver.find_element_by_id("{}".format(rand_pref_div))
    # Click on the selected preference option
    pref.click()
    # Wait for 2 seconds
    sleep(2)

    # List of IDs for demographic options
    demo_div = ['i161', 'i164', 'i167', 'i170']
    # Select a random demographic option from the list
    rand_demo_div = demo_div[randint(0, 3)]
    # Find the demographic option element by its ID
    demo = driver.find_element_by_id("{}".format(rand_demo_div))
    # Click on the selected demographic option
    demo.click()
    # Wait for 2 seconds
    sleep(2)

    # List of IDs for rural/urban options
    rur_div = ['i177', 'i180', 'i183']
    # Select a random rural/urban option from the list
    rand_rur_div = rur_div[randint(0, 2)]
    # Find the rural/urban option element by its ID
    rur = driver.find_element_by_id("{}".format(rand_rur_div))
    # Click on the selected rural/urban option
    rur.click()
    # Wait for 2 seconds
    sleep(2)

    # List of IDs for purchase options
    pur_div = ['i190', 'i193', 'i196', 'i199']
    # Select a random purchase option from the list
    rand_pur_div = pur_div[randint(0, 3)]
    # Find the purchase option element by its ID
    pur = driver.find_element_by_id("{}".format(rand_pur_div))
    # Click on the selected purchase option
    pur.click()
    # Wait for 2 seconds
    sleep(2)

    # List of IDs for middle options
    mid_div = ['i206', 'i209', 'i212']
    # Select a random middle option from the list
    rand_mid_div = mid_div[randint(0, 2)]
    # Find the middle option element by its ID
    mid = driver.find_element_by_id("{}".format(rand_mid_div))
    # Click on the selected middle option
    mid.click()
    # Wait for 2 seconds
    sleep(2)

    # List of IDs for time options
    tim_div = ['i219', 'i222', 'i225', 'i228']
    # Select a random time option from the list
    rand_tim_div = tim_div[randint(0, 3)]
    # Find the time option element by its ID
    tim = driver.find_element_by_id("{}".format(rand_tim_div))
    # Click on the selected time option
    tim.click()
    # Wait for 2 seconds
    sleep(2)

    # Generate a random number between 1 and 10 for the level option
    opt = randint(1, 10)
    # Find the level option element by its data-value
    lev = driver.find_element_by_xpath('//div[@data-value="{}"]'.format(opt))
    # Click on the selected level option
    lev.click()
    # Wait for 2 seconds
    sleep(2)

    # Wait for 4 seconds
    sleep(4)

    # Find the submit button by its jsname
    sn_b = driver.find_element_by_xpath('//div[@jsname="M2UYVd"]')
    # Click the submit button
    sn_b.click()
    # Wait for 2 seconds
    sleep(2)
    
    # Wait for 2 seconds
    sleep(2)
    
    # Find and click the "Submit another response" link to prepare for the next submission
    driver.find_element_by_link_text("Submit another response").click()
    # Wait for 2 seconds
    sleep(2)
    # Increment the counter
    count += 1

# Close the browser after completing all submissions
driver.quit()