# Twilio is an SMS gateway service,
# which means it’s a service that allows you to send text messages from your
# programs. 
# If you prefer not to use Twilio,
# you can find alternative services by searching online for free sms gateway,
# python sms api, or even twilio alternatives
# Before signing up for a Twilio account, install the twilio module.

from twilio.rest import TwilioRestClient
accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '+14955551234'
myCellPhone = '+14955558888'
message = twilioCli.messages.create(body='Mr. Watson - Come here - I want to see you.', from_=myTwilioNumber, to=myCellPhone)

# The call to TwilioRestClient() returns a TwilioRestClient object v. This object has a mes-
# sages attribute, which in turn has a create() method you can use to send text
# messages. This is the method that will instruct Twilio’s servers to send your
# text message. After storing your Twilio number and cell phone number in
# myTwilioNumber and myCellPhone, respectively, call create() and pass it keyword
# arguments specifying the body of the text message, the sender’s number
# (myTwilioNumber), and the recipient’s number (myCellPhone)




# Test in the cmd:
>>> message.to
'+14955558888'
>>> message.from_
'+14955551234'
>>> message.body
'Mr. Watson - Come here - I want to see you.'

>>> message.status
'queued'
>>> message.date_created
datetime.datetime(2015, 7, 8, 1, 36, 18)
>>> message.date_sent == None
True

>>> message.sid
'SM09520de7639ba3af137c6fcb7c5f4b51'
>>> updatedMessage = twilioCli.messages.get(message.sid)
>>> updatedMessage.status
'delivered'
>>> updatedMessage.date_sent
datetime.datetime(2015, 7, 8, 1, 36, 18)


# Unfortunately, receiving text messages with Twilio is a bit more complicated than sending them Twilio requires that you have a website running its own web application 
