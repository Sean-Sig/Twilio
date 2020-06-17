from twilio.rest import Client

account_sid = "TWILIO_ACCOUNT_SID"
auth_token = "TWILIO_AUTH_TOKEN"

client = Client(account_sid, auth_token)

client.messages.create(
    to="phonenumber you are trying to send",
    from_="+12562914037",
    body="This is the content of the message being sent"
)