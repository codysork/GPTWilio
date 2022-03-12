from twilio.rest import Client as TwilioClient


class EasyClient(TwilioClient):
    """A Twilio client that is easier to work with."""

    class CannotSend(Exception):
        pass

    def __init__(self, phone_number: str = None, text_message: str = None):
        self.phone_number = phone_number
        self.text_message = text_message

    def sms(self, phone_number: str = None, text_message: str = None) -> object:
        """Sends a text message to a specified phone number."""
        if not phone_number:
            if self.phone_number:
                phone_number = self.phone_number
            else:
                raise self.CannotSend()
            if not self.text_message:
                raise self.CannotSend()
        if not text_message:
            raise self.CannotSend()

        return self.messages.create(
            messaging_service_sid='NEEDS_TO_BE_REPLACED',
            body=text_message,
            to=phone_number)
