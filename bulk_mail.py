import smtplib
import csv
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Sensitive Informations - These should be stored securely, not directly in the code.
# Using environment variables or a secure configuration file is recommended.
MY_EMAIL = "myfriendhammad@gmail.com"
MY_PASSWORD = "Hammaad 13"

# Establish a connection to the SMTP server
s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login(MY_EMAIL, MY_PASSWORD)

count = 1

# Read data from the CSV file
dataset = csv.reader(open("bulk_mail.csv", "r"), delimiter=',')
print(dataset)
next(dataset)  # Skip the header row

# Iterate through each row in the dataset
for row in dataset:
    """Sends a personalized email to each recipient in the CSV file.

    Args:
        row: A list representing a row in the CSV file, where the first element
          is the recipient's name and the second is their email address.
    """
    msg = MIMEMultipart()
    content = Template("Dear ${NAME} \n \t This a custom bulk email generator script built by"
                       "Mohammed Hammaad Mateen of PESU ECC"
                       "for BizEdge Disha during the internship\nThank You")
    subject = Template("This custom bulk email is dedicated to ${NAME}")
    content = content.substitute(NAME=row[0])
    subject = subject.substitute(NAME=row[0])
    msg['From'] = MY_EMAIL
    msg['To'] = row[1]
    msg['Subject'] = subject
    msg.attach(MIMEText(content, 'plain'))
    s.send_message(msg)
    print(count, "Sent to", row[0], "-->", row[1])
    count += 1
    del msg  # Delete the message object after sending

print("\n\nSuccessfully sent mails to ", count - 1, " recipients")
print("Alhamdulillah")
s.quit()