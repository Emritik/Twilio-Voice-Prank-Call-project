#import library

import os
from twilio.rest import Client

#neter your account_sid and auth_token

account_sid = os.environ['AC087d7d180bf753f0993c3846b729e72e']
auth_token = os.environ['8587cc122360d7fe71a11d0172a18242']
client = Client(account_sid, auth_token)

#enter your freind number in "to" section.
#enter a twilio number (which is buy form console twilio) in "from-" section.

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+19285978342',
                        from_='+919125545701'
                        )

print(call.sid)
