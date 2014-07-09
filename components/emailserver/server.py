__author__ = 'haukurk'

import smtpd
from .mail import message_from_string
from components.emailserver import watcher

email_watcher = watcher.EmailWatcher()


class CustomSMTPServer(smtpd.DebuggingServer):
    """
    SMTP Server that listens to email and returns it
    """

    def process_message(self, peer, mailfrom, rcpttos, data):
        email_watcher.triggerEmail(message_from_string(data))
        return
