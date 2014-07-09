__author__ = 'haukurk'

from components.emailserver.server import email_watcher
from components.smsinterpreter import sms
import asyncore
from utils.logger import logger


def component_proxy(message):
    """
    Proxy between email component and sms interpreter.
    Email component event returns an email.Message object and the interpreter takes 2 arguments:
        text and a mobile number.
    """
    response_dictionary = sms.send_sms(str(message["To"].split('@')[0]), message.get_payload())

    if response_dictionary["status"] == 200:
        logger.info("SMS Sent out successfully to: " + str(message["To"].split('@')[0]))
    else:
        logger.info("SMS Sent out to " + str(message["To"].split('@')[0]) + " with the status code: " + str(
            response_dictionary["status"]))

# Listen for emails and deliver event to the component proxy.
email_watcher.emailArrived += component_proxy

print "Bridge started! We are listening on port 25."
logger.info("Bridge started! We are listening on port 25.")

# Leave for LAST. Listen for email events from async socket handler for email server.
asyncore.loop()