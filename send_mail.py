import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)  # or for ssl connection, smtplib.SMTP_SSL()
smtpObj.ehlo() # Hello Message
smtpObj.starttls() #enables encryption for your connection.  if you use port 465, ssl, no need to use this line
smtpObj.login('*****@gmail.com', 'Dipu2018@$%')
smtpObj.sendmail('*****@gmail.com', '***Abid1@proton.me', 'Subject: Hello.\nDear my love...')
smtpObj.quit()


# Gmail     smtp.gmail.com
# Outlook.com/Hotmail.com   smtp-mail.outlook.com
# Yahoo     smtp.mail.yahoo.com
# AT&T      smpt.mail.att.net (port 465)
# Comcast   smtp.comcast.net
# Verizon   smtp.verizon.net (port 465)

# The sendmail() method requires three arguments.
# • Your email address as a string (for the email’s “from” address)
# • The recipient’s email address as a string or a list of strings for multiple
# recipients (for the “to” address)
# • The email body as a string
# The start of the email body string must begin with 'Subject: \n' for the
# subject line of the email. The '\n' newline character separates the subject
# line from the main body of the email