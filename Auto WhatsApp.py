"""
A script to automate sending messages on WhatsApp Web using Selenium.

Pre-requisites:
    - Chrome Driver: Ensure you have the correct ChromeDriver installed and in your system's PATH.
    - Selenium WebDriver: Install the Selenium package using `pip install selenium`.
    - Python: Python 3.6 or higher.
    - WhatsApp Account: An active WhatsApp account linked to a phone.

WorkFlow:
    1.  Run this script. Selenium will open a Chrome browser with WhatsApp Web.
    2.  Scan the WhatsApp QR Code using your phone when prompted.
    3.  The script will then prompt you to choose a contact to message.
    4.  You will then be prompted to select the type of message:
        - Text
        - Document
        - Image/Video
    5.  Enter the message or the file path, as required.
    6.  If the message is sent successfully, the process repeats until the user chooses to exit.

Interrupts:
    - Enter '!R' at any message prompt to restart the message sending process.
    - Type 'Take Me Out Of WhatsApp!!' to quit the script.

Credits:
    - Scripted with love by Mohammed Hammaad Mateen
    - GitHub Profile: MohammedHMateen
    - You are free to use it for the betterment of society.
"""
from selenium import webdriver
from time import sleep

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

ok = "I've scanned the QR"
go = "Take Me Out Of WhatsApp!!"
qr = "Qr code"
go_i = "WA"

# Wait for user to scan the QR code
while(qr!=ok):
    print("Please Scan the WhatsApp QR Code and Type the following to proceed:\n",ok,"\n")
    qr=input()

"""
WhatsApp Class and Attributes
These selectors might change in future, keep an eye on them in the WhatsApp web page's HTML.
"""
uk_recp_url = 'https://web.whatsapp.com/send?phone=%2B91{}&amp;text&amp;app_absent=0'
txtbox_class = '_1hRBM'
att_span = 'clip'
ivbt_ip = 'image/*,video/mp4,video/3gpp,video/quicktime'
docbt_ip = '*'
snd_span = 'send'

# Main loop for sending messages
while (go_i!=go):
    # Input the recipient's name
    per=input("Enter the recipient: ")
    # Find the recipient in the contacts list
    try:
      persn = driver.find_element_by_xpath('//span[@title="{}"]'.format(per))
      persn.click()
    except Exception as e:
      print(f"Recipient '{per}' not found. Please check the name and try again.")
      continue

    # Input message type
    mg_type=int(input("Please Press:\n1: For text message\n2: For sending a document file\n3: For sending an image/video file\n4: To Restart\n"))
    if mg_type==1:
        # Text message
        mg = input("Enter the message to send or !R to restart\n")
        if (mg=='!R'):
            continue
        # Find the message input box
        mg_box= driver.find_element_by_class_name("{}".format(txtbox_class))
        mg_box.click()
        mg_box.send_keys(mg)
        # Find and click the send button
        sn_b = driver.find_element_by_xpath('//span[@data-testid="{}"]'.format(snd_span))
        sn_b.click()

    elif mg_type==2:
        # Document message
        file = input('Enter the filepath to send the document or !R to restart\n:')
        if (file=='!R'):
            continue
        # Find and click the attachment button
        attach_box = driver.find_element_by_xpath('//span[@data-testid="{}"]'.format(att_span))
        attach_box.click()
        sleep(2) # Wait for the attachment menu to load
        # Find the document input box and send the file path
        doc_box = driver.find_element_by_xpath('//input[@accept="{}"]'.format(docbt_ip))
        doc_box.send_keys(file)
        sleep(4) # Wait for the file to upload
        # Find and click the send button
        sn_b = driver.find_element_by_xpath('//span[@data-testid="{}"]'.format(snd_span))
        sn_b.click()

    elif mg_type==3:
        # Image/Video message
        file = input('Enter the filepath to send the image/video or !R to restart\n:')
        if (file=='!R'):
            continue
        # Find and click the attachment button
        attach_box = driver.find_element_by_xpath('//span[@data-testid="{}"]'.format(att_span))
        attach_box.click()
        sleep(2) # Wait for the attachment menu to load
        # Find the image/video input box and send the file path
        iv_box = driver.find_element_by_xpath('//input[@accept="{}"]'.format(ivbt_ip))
        iv_box.send_keys(file)
        sleep(4) # Wait for the file to upload
        # Find and click the send button
        sn_b = driver.find_element_by_xpath('//span[@data-testid="{}"]'.format(snd_span))
        sn_b.click()

    else:
        print("Wrong Option!! Restarting ....")
        continue
    
    # Check if the user wants to continue or exit
    go_i=input("Enter any key to continue\nOR type: Take Me Out Of WhatsApp!! : to exit \n")

# Exit gracefully
print("Exiting Gracefully out of WhatsApp....")
sleep(2)
driver.quit()
sleep(4)
print("Alhamdulillah")

"""
    -->Unkowns WA Chat (Example URL)
        https://web.whatsapp.com/send?phone=%2B918310428928&amp;text&amp;app_absent=0

    -->QR code html tag (Example HTML snippet)
        <div class="_1yHR2" data-ref="1@apjWZIPoOxQEZhOm3sO2yKu1yiN0CANlICg1B6mf4EJagHut03EUv7yR5od6Q7mVtqdMNlLvsF6hCA==,5GRfoudVKeCpEKGMcq8fUUykvjGFSeFKWaj/Xb3HmUU=,s4IAEx/zW2lGT1M6xl2diQ=="><span>

    -->img captions // inner html (Example HTML snippet)
        <div class="_1awRl copyable-text selectable-text" contenteditable="true" data-tab="6" dir="ltr" spellcheck="true">This is the cap sn d the key here</div>

    -->img/doc alt-add (Example HTML snippet)
        <span data-testid="add-alt" data-icon="add-alt" class="">
        alt_span=add-alt
        '//span[@data-testid="{}"]'.format(alt_span)
"""