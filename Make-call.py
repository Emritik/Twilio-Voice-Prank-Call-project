#import library

import os
from twilio.rest import Client

#Enter your  twilio account_sid and auth_token

account_sid = os.environ['enter here your account sid']
auth_token = os.environ['enter here your auth token no.']
client = Client(account_sid, auth_token)

#enter your freind number in "to" section.
#enter a twilio number (which is buy form console twilio) in "from-" section.

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+19285978342',
                        from_='+919125545701'
                        )

print(call.sid)
