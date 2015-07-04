import smtplib
SERVER = "smtp.gmail.com"
FROM = "@Sendergmail.com"
TO = ["Receiver@gmail.com"] # must be a list

SUBJECT = "Hello!"
TEXT = "This is a test of emailing through smtp in google."

# Prepare actual message
message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail
server = smtplib.SMTP(SERVER, 587)
server.ehlo()
server.starttls()
server.login(FROM, 'password')
server.sendmail(FROM, TO, message)
server.quit()
