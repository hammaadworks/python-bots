from selenium import webdriver
from time import sleep
from random import randint
from faker import Faker

# Initialize Faker for generating fake data.
fake = Faker("en_IN")
# Initialize a counter for the loop.
count = 0
# Set the number of times the loop should execute.
loop_till = 50


def fill_google_form(driver: webdriver.Chrome, fake: Faker) -> None:
    """Fills out a Google Form with randomly generated fake data.

    This function navigates to a specified Google Form URL, and then
    iteratively populates the form fields with random data generated
    using the Faker library and random integers. It handles name,
    gender, age, height, weight, family members, money, and sport preferences.

    Args:
        driver: A Selenium Chrome webdriver instance.
        fake: A Faker instance for generating fake data.
    """
    sleep(6)
    # Name field population
    name_field = driver.find_element_by_xpath('//input[@aria-labelledby="i1"]')
    name_field.click()
    sleep(2)
    name = fake.unique.name()
    name_field.send_keys(name)
    sleep(2)

    # Gender selection
    gender_div = ['i9', 'i12']
    rand_gender_div = gender_div[randint(0, 1)]
    gender = driver.find_element_by_id(f"{rand_gender_div}")
    gender.click()
    sleep(2)

    # Age field population
    age_field = driver.find_element_by_xpath('//input[@aria-labelledby="i15"]')
    age_field.click()
    sleep(2)
    age = randint(10, 20)
    age_field.send_keys(age)
    sleep(2)

    # Height selection
    height_div = ['i23', 'i26', 'i29', 'i32']
    rand_height_div = height_div[randint(0, 3)]
    height = driver.find_element_by_id(f"{rand_height_div}")
    height.click()
    sleep(2)

    # Weight field population
    weight_field = driver.find_element_by_xpath('//input[@aria-labelledby="i35"]')
    weight_field.click()
    sleep(2)
    weight = randint(30, 90)
    weight_field.send_keys(weight)
    sleep(2)

    # Family members field population
    fam_field = driver.find_element_by_xpath('//input[@aria-labelledby="i39"]')
    fam_field.click()
    sleep(2)
    fam = randint(3, 10)
    fam_field.send_keys(fam)
    sleep(2)

    # Money selection
    mony_div = ['i47', 'i50', 'i53', 'i56', 'i59', 'i62']
    rand_mony_div = mony_div[randint(0, 5)]
    mony = driver.find_element_by_id(f"{rand_mony_div}")
    mony.click()
    sleep(2)

    # Sport selection
    sport_div = ['i69', 'i72', 'i75', 'i78', 'i81']
    rand_sport_div = sport_div[randint(0, 4)]
    sport = driver.find_element_by_id(f"{rand_sport_div}")
    sport.click()
    sleep(2)
    sleep(4)

    # Submit button click
    sn_b = driver.find_element_by_xpath('//div[@jsname="M2UYVd"]')
    sn_b.click()
    sleep(2)


if __name__ == "__main__":
    """Main execution block for filling the Google Form multiple times.

    This block initializes a Chrome webdriver, navigates to the target Google Form,
    and then iteratively calls the fill_google_form function to submit the form
    multiple times according to the `loop_till` variable. It then closes the browser.
    """
    driver = webdriver.Chrome()
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfsw_XJVOoFRzmJYehTFm3HpW_x5zKzmuGH_jPi4V9EX5paxQ/viewform?usp=sf_link")

    while count < loop_till:
        fill_google_form(driver, fake)
        driver.find_element_by_link_text("Submit another response").click()
        sleep(2)
        count += 1

    driver.quit()