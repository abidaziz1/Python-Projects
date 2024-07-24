#  here’s a full example of logging in to an IMAP server,
# searching for emails, fetching them, and then extracting the text of the
# email messages from them.

import imapclient
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)

imapObj.logi('dipu***@gmail.com', 'Dipu2018@$%')
# For Gmail accounts, you may need to use an application-specific password;
imapObj.select_folder('INBOX', readonly=True)
# To select a folder to search through, pass the folder’s name as a stringinto the IMAPClient object’s select_folder() method.
# readonly=True keyword argument. Doing this will prevent you from
# accidentally deleting an email—but it also means that emails will not get
# marked as read if you fetch them with the fetch() method. If you do want
# emails to be marked as read when you fetch them, you will need to pass
# readonly=False to select_folder(). 
UIDs = imapObj.search(['SINCE 05-Dec-2023'])
# UIDs nicher moto ashbe
# [40032, 40033, 40034, 40035, 40036, 40037, 40038, 40039, 40040, 40041]
rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
# >>> import pprint
# >>> pprint.pprint(rawMessages)

# this return value is a nested dictionary of messages with UIDs as the keys.
# Each message is stored as a dictionary with two keys: 'BODY[]' and 'SEQ'.
# The 'BODY[]' key maps to the actual body of the email. The 'SEQ' key is for a
# sequence number, which has a similar role to the UID. You can safely ignore it.

# The search() method doesn’t return the emails themselves but rather
# unique IDs (UIDs) for the emails, as integer values. You can then pass these
# UIDs to the fetch() method to obtain the email content.

# Here are some example search() method calls along with their meanings:
# imapObj.search(['ALL']) Returns every message in the currently
# selected folder.
# imapObj.search(['ON 05-Jul-2015']) Returns every message sent on
# July 5, 2015.
# Sending Email and Text Messages 371
# imapObj.search(['SINCE 01-Jan-2015', 'BEFORE 01-Feb-2015', 'UNSEEN'])
# Returns every message sent in January 2015 that is unread. (Note that
# this means on and after January 1 and up to but not including February 1.)
# imapObj.search(['SINCE 01-Jan-2015', 'FROM alice@example.com']) Returns
# every message from alice@example.com sent since the start of 2015.
# imapObj.search(['SINCE 01-Jan-2015', 'NOT FROM alice@example.com'])
# Returns every message sent from everyone except alice@example.com
# since the start of 2015.
# imapObj.search(['OR FROM alice@example.com FROM bob@example.com']) Returns
# every message ever sent from alice@example.com or bob@example.com.
# imapObj.search(['FROM alice@example.com', 'FROM bob@example.com']) Trick
# example! This search will never return any messages, because messages
# must match all search keywords. Since there can be only one “from”
# address, it is impossible for a message to be from both alice@example.com
# and bob@example.com.

import pyzmail
message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
message.get_subject()  # subject show korbe
message.get_addresses('from') # ('Edward Snowden', 'esnowden@nsa.gov')
message.get_addresses('to')
message.get_addresses('cc')
message.get_addresses('bcc')

message.text_part != None  # True
message.text_part.get_payload().decode(message.text_part.charset)
message.html_part != None  # True
message.html_part.get_payload().decode(message.html_part.charset)
imapObj.logout()
# Emails can be sent as plaintext, HTML, or both. Plaintext emails contain
# only text, while HTML emails can have colors, fonts, images, and other fea-
# tures that make the email message look like a small web page. If an email
# is only plaintext, its PyzMessage object will have its html_part attributes set to
# None. Likewise, if an email is only HTML, its PyzMessage object will have its
# text_part attribute set to None.



# Deleting mails
>>> imapObj.select_folder('INBOX', readonly=False)
>>> UIDs = imapObj.search(['ON 09-Jul-2015'])
>>> UIDs
[40066]
>>> imapObj.delete_messages(UIDs)
{40066: ('\\Seen', '\\Deleted')}
>>> imapObj.expunge()
('Success', [(5452, 'EXISTS')])
