#Jameka Echols 
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACdf7825efd19c0f9c084a2d62dcf1004b"
# Your Auth Token from twilio.com/console
auth_token  = "32543c73a464d04c890b663356350a25"


client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16189779837", # must be from a verified number that I added to account 
    from_="+16152099156", # number generated by twilio
    body="This meka! I'm texting from a program I made haha love ya")

print(message.sid)
