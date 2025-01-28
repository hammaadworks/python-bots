from selenium import webdriver
from time import sleep
from random import *


def main():
    """
    Navigates to a Google Merchant Center page, enters an email address, and pauses.

    This script uses Selenium to automate browser actions. It opens a Chrome browser,
    navigates to a specific Google Merchant Center URL, waits for 4 seconds,
    enters a hardcoded email address into the email input field, and then pauses again for 4 seconds.

    Note:
        The script includes commented-out lines that suggest further actions,
        such as clicking elements and entering text, which are not implemented.

    Raises:
        selenium.common.exceptions.WebDriverException: If there is an issue with the WebDriver setup.
        selenium.common.exceptions.NoSuchElementException: If elements cannot be found on the page.
    """

    driver = webdriver.Chrome()
    try:
        driver.get(
            "https://merchants.google.com/mc/products/sources?a=284456364&hl=en&fmp=1&utm_id=gfr&utm_source=google.com&utm_medium=referral&gfr_referral=true&mcsubid=us-en-web-g-mc-gfr"
        )
        sleep(4)

        email_field = driver.find_element_by_xpath("//input[@type='email']")
        email_field.send_keys("myfriendhammad@gmail.com")
        # driver.find_element_by_xpath("").click()
        # driver.find_element_by_xpath("").send_keys("Hammaad 13")
        # driver.find_element_by_xpath("").click()
        sleep(4)
    finally:
       driver.quit()


if __name__ == "__main__":
    main()