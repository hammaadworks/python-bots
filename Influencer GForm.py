from random import randint
from time import sleep

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

FORM_RESPONSES = 20
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdlgw7gYP9NHJtg15MWGTQGkW4yeIGbyWIe1X7MFKsgt8VD3A/viewform"
INIT_PAUSE = 4
EVENT_PAUSE = 1

fake = Faker("en_IN")
driver = webdriver.Chrome()
driver.get(FORM_URL)


def radio_select_element(starting_id, option_count, default_select=None, radio_distance=3, description=""):
    if default_select is None:
        default_select = randint(0, option_count - 1)
    selected_id = starting_id + (radio_distance * default_select)
    driver.find_element(by=By.ID, value=f'i{selected_id}').click()
    sleep(EVENT_PAUSE)
    print(f"Chose option: {default_select + 1}, id: {selected_id}, radio element: {description}")
    return default_select


def text_element(xpath_id, text, description=""):
    text_field = driver.find_element(by=By.XPATH, value=f'//input[@aria-labelledby="{xpath_id}"]')
    text_field.click()
    sleep(EVENT_PAUSE)
    text_field.send_keys(text)
    print(f"Typed {text} on text element: {description}")
    sleep(EVENT_PAUSE)


def get_gender():
    # returns 0 for male and 1 for female
    return 1 if randint(1, 2) % 2 else 0


def submit_form_reopen(submit_button_xpath):
    sn_b = driver.find_element(by=By.XPATH, value=f'{submit_button_xpath}')
    sn_b.click()
    sleep(EVENT_PAUSE)
    driver.find_element(by=By.LINK_TEXT, value="Submit another response").click()
    sleep(EVENT_PAUSE)


for i in range(FORM_RESPONSES):
    print(f"Filling form {i + 1}/{FORM_RESPONSES}")
    sleep(INIT_PAUSE)
    is_female = get_gender()

    name = fake.name_female() if is_female else fake.name_male()
    text_element(xpath_id='i1', text=name, description="name")

    radio_select_element(starting_id=9, option_count=2, default_select=is_female, description="gender")

    radio_select_element(starting_id=19, option_count=4, description="age")

    radio_select_element(starting_id=35, option_count=5, description="social media")

    radio_select_element(starting_id=54, option_count=6, description="influencer type")

    radio_select_element(starting_id=76, option_count=5, description="influencer factors")

    radio_select_element(starting_id=95, option_count=4, description="content type")

    radio_select_element(starting_id=111, option_count=2, description="more informed")

    radio_select_element(starting_id=121, option_count=3, description="influenced")

    radio_select_element(starting_id=134, option_count=2, description="research")

    radio_select_element(starting_id=144, option_count=2, description="fomo")

    is_no = radio_select_element(starting_id=154, option_count=2, description="trust")

    if not is_no:
        radio_select_element(starting_id=164, option_count=3, description="trust yes")
    else:
        radio_select_element(starting_id=177, option_count=4, description="trust no")

    radio_select_element(starting_id=193, option_count=2, description="recall")

    is_no = radio_select_element(starting_id=203, option_count=2, description="bought")

    if not is_no:
        radio_select_element(starting_id=213, option_count=5, description="bought yes")

    radio_select_element(starting_id=232, option_count=2, description="set trends")

    radio_select_element(starting_id=242, option_count=2, description="enhance trends")

    radio_select_element(starting_id=252, option_count=2, description="helped")

    submit_form_reopen('//div[@jsname="M2UYVd"]')
    print(f"Done Filling form {i + 1}/{FORM_RESPONSES}")
    print("\n\n---------------------------Alhamdulillah-------------------------------\n\n")

driver.quit()
