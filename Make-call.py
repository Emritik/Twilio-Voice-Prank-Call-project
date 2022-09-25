#import library

import os
from twilio.rest import Client

#Enter your Twilio Account SID and Auth Token.

account_sid = os.environ['enter here your Account SID : ']
auth_token = os.environ['enter here your Auth Token : ']
client = Client(account_sid, auth_token)




call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='XXXXXXXXX',      #Enter your friend's number in "to" section.
                        from_='+91XXXXXXXXXX'   #Enter your twilio number ( which bought from Twilio console ) in "from_" section.
                        )

print(call.sid)
