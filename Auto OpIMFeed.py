from selenium import webdriver
from time import sleep
from random import *

def navigate_and_interact_with_infinique_backend():
    """Navigates to the Infinique backend, logs in, and navigates to the feed manager.

    This function automates the process of logging into the Infinique backend,
    navigating to the WordPress admin panel, scrolling to the bottom of the page,
    and then clicking on the product feed manager icon.

    It utilizes Selenium WebDriver to interact with the web page elements.
    """
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.infiniquemall.com/infiniquebackend.php")
        sleep(4)

        # Find and interact with the username input field.
        username_field = driver.find_element_by_xpath("//input[@id='user_login']")
        username_field.click()
        username_field.send_keys('devteam')

        # Find and interact with the password input field.
        password_field = driver.find_element_by_xpath("//input[@id='user_pass']")
        password_field.click()
        password_field.send_keys('OKQXxI*1!RB^0rze1L8aiAfZ')

        # Click the submit button to log in.
        driver.find_element_by_xpath("//input[@type='submit']").click()
        sleep(2)

        # Navigate to the WordPress admin panel.
        driver.find_element_by_xpath("//a[@href='https://www.infiniquemall.com/wp-admin/']").click()
        sleep(4)

        # Scroll to the bottom of the page.
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        sleep(2)

        # Click the product feed manager icon.
        driver.find_element_by_xpath("//img[@src='https://www.infiniquemall.com/wp-content/plugins/wp-product-feed-manager/images/app-rss-plus-xml-icon.png']").click()
        sleep(4)

    finally:
        # Close the browser window when done or if an error occurs.
        driver.quit()


if __name__ == '__main__':
    navigate_and_interact_with_infinique_backend()