'''
    Pre-requisites:
    Chrome Driver
    Selenium WebDriver
    Python
    
    WorkFlow:
    Run this script and selenium will open a Chrome browser with WhatsApp Web

    Scan the WhatsApp QR Code once

    Choose the person from your contacts whom you would like to send the message to.

    Choose the type of message to send
        Text
        Document
        Image/Video

    Enter the message

    If Success, the process repeats infinitely
    
    Interrupts: 
    Hit--  --to Go Back 1 Level
    Hit--  --to Restart
    Type-- Take Me Out Of WhatsApp!! --to Quit

@Credits - Scripted with love by Mohammed Hammaad Mateen
GitHub Profile - MohammedHMateen
You are free to use it for the betterment of the society.
'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

ok = "I've scanned the QR"
go = "Take Me Out Of WhatsApp!!"
qr = "Qr code"
go_i = "WA"

while(qr!=ok):
    print("Please Scan the WhatsApp QR Code and Type the following to proceed:\n",ok,"\n")
    qr=input()

'''
    WhatsApp Class and Attributes
    These might change in future keep a look
'''
uk_recp_url = 'https://web.whatsapp.com/send?phone=%2B91{}&amp;text&amp;app_absent=0'
txtbox_class = '_1hRBM'
att_span = 'clip'
ivbt_ip = 'image/*,video/mp4,video/3gpp,video/quicktime'
docbt_ip = '*'
snd_span = 'send'



while (go_i!=go):

    per=input("Enter the recipient: ")
    persn = driver.find_element_by_xpath('//span[@title="{}"]'.format(per))
    persn.click()

    mg_type=int(input("Please Press:\n1: For text message\n2: For sending a document file\n3: For sending an image/video file\n4: To Restart\n"))
    if mg_type==1:
        mg = input("Enter the message to send or !R to restart\n")
        if (mg=='!R'):
            continue
        mg_box= driver.find_element_by_class_name("{}".format(txtbox_class))
        mg_box.click()
        mg_box.send_keys(mg)
        sn_b = driver.find_element_by_xpath('//span[@data-testid="{}"]'.format(snd_span))
        sn_b.click()

    elif mg_type==2:
        file = input('Enter the filepath to send the document or !R to restart\n:')
        if (file=='!R'):
            continue
        attach_box = driver.find_element_by_xpath('//span[@data-testid="{}"]'.format(att_span))
        attach_box.click()
        sleep(4)
        doc_box = driver.find_element_by_xpath('//input[@accept="{}"]'.format(docbt_ip))
        doc_box.send_keys(file)
        sleep(4)
        sn_b = driver.find_element_by_xpath('//span[@data-testid="{}"]'.format(snd_span))
        sn_b.click()

    elif mg_type==3:
        file = input('Enter the filepath to send the document or !R to restart\n:')
        if (file=='!R'):
            continue
        attach_box = driver.find_element_by_xpath('//span[@data-testid="{}"]'.format(att_span))
        attach_box.click()
        sleep(4)
        iv_box = driver.find_element_by_xpath('//input[@accept="{}"]'.format(ivbt_ip))
        iv_box.send_keys(file)
        sleep(4)
        sn_b = driver.find_element_by_xpath('//span[@data-testid="{}"]'.format(snd_span))
        sn_b.click()

    else:
        print("Wrong Option!! Restarting ....")
        continue
    
    go_i=input("Enter any key to continue\nOR type: Take Me Out Of WhatsApp!! : to exit \n")

print("Exiting Gracefully out of WhatsApp....")
sleep(2)
driver.quit()
sleep(4)
print("Alhamdulillah")

'''
    -->Unkowns WA Chat
        https://web.whatsapp.com/send?phone=%2B918310428928&amp;text&amp;app_absent=0

    -->QR code html tag
        <div class="_1yHR2" data-ref="1@apjWZIPoOxQEZhOm3sO2yKu1yiN0CANlICg1B6mf4EJagHut03EUv7yR5od6Q7mVtqdMNlLvsF6hCA==,5GRfoudVKeCpEKGMcq8fUUykvjGFSeFKWaj/Xb3HmUU=,s4IAEx/zW2lGT1M6xl2diQ=="><span>

    -->img captions // inner html
        <div class="_1awRl copyable-text selectable-text" contenteditable="true" data-tab="6" dir="ltr" spellcheck="true">This is the cap sn d the key here</div>

    -->img/doc alt-add
        <span data-testid="add-alt" data-icon="add-alt" class="">
        alt_span=add-alt
        '//span[@data-testid="{}"]'.format(alt_span)
'''
