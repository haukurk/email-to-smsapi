__author__ = 'haukurk'

from components.smsinterpreter.apiclient.cmclient import CMClient
import config
import utils

# Institate the API client.
api = CMClient(config.API_USERNAME, config.API_PASSWORD, config.API_CUSTOMER_NUMBER, config.SMS_SENDER_NAME,
               config.SMS_TARIFF)


def send_sms(number, text):
    """
    Send SMS with API SMS client.
    """
    return api.postxml('/', utils.createCMxml(config.API_CUSTOMER_NUMBER, config.API_USERNAME,
                                              config.API_PASSWORD, config.SMS_TARIFF, config.SMS_SENDER_NAME,
                                              text, number))
