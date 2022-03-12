from twilio.rest import Client as TwilioClient


class EasyClient(TwilioClient):
    """A Twilio client that is easier to work with."""

    def sms(self, phone_number: str, text: str):
        """Sends a text message to a specified phone number."""
        self.messages.create(
            messaging_service_sid='NEEDS_TO_BE_REPLACED',
            body=text,
            to=phone_number)
