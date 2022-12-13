from twilio.rest import Client

TWILIO_SID = "AC631d95d3ebf7d27c395ab8798811714a"
TWILIO_AUTH_TOKEN = "f9f4cffa5f9487ce8ffd4470f16974c7"
TWILIO_VIRTUAL_NUMBER = "+13854627318"
TWILIO_VERIFIED_NUMBER = "+351961178759"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)