
# coding: utf-8

# In[ ]:


import sys
from smtplib import SMTP as SMTP
from email.mime.text import MIMEText

# credentials masked, obviously
SMTPserver = 'xx '
sender = 'xx '
destination = ['xx@xx.com','xx@xx.com']

USERNAME = ""
PASSWORD = ""

# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'

content = """xxxx
"""

subject = "xxxx"

try:
    msg = MIMEText(content, text_subtype)
    msg['Subject'] = subject
    msg['From'] = sender
    conn = SMTP(host=SMTPserver, port=587)  # object created
    conn.ehlo() 
    conn.starttls()  # enable TLS
    conn.ehlo()
    conn.set_debuglevel(False)
    conn.login(USERNAME, PASSWORD)

    try:
        conn.sendmail(sender, destination, msg.as_string())
        print("Email is sent")
    finally:
        conn.quit()

except Exception as exc:
    sys.exit("mail failed; %s" % str(exc))

