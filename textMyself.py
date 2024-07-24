# If you’ve automated a boring task with a program that takes
# a couple of hours to run, you could have it notify you with a text when it’s
# finished. Or you may have a regularly scheduled program running that
# sometimes needs to contact you, such as a weather-checking program that
# texts you a reminder to pack an umbrella.



# Preset values:
accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
myNumber = '+15559998888'
twilioNumber = '+15552225678'
from twilio.rest import TwilioRestClient
def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)

# If you want to make the textmyself() function available to your other programs, simply place the textMyself.py file in the same folder 
# import textmyself
# textmyself.textmyself('The boring task is finished.')
