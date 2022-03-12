from twilio.rest import Client as TwilioClient


class EasyClient(TwilioClient):
    """A Twilio client that is easier to work with."""

    class CannotSend(Exception):
        pass

    def __init__(self, phone_number: str, text: str):
        self.phone_number = phone_number
        self.text = text

    def sms(self, phone_number: str = None, text: str = None) -> object:
        """Sends a text message to a specified phone number."""
        if not phone_number or not text:
            throw CannotSend()
        return self.messages.create(
            messaging_service_sid='NEEDS_TO_BE_REPLACED',
            body=text,
            to=phone_number)
