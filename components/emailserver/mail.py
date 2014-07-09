__author__ = 'haukurk'

import email


def message_from_string(message_data):
    """
    Convert data of an email message to message object.
    """

    return email.message_from_string(message_data)