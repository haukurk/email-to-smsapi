__author__ = 'haukurk'

from components.events import Event


class EmailWatcher:
    """
    Watcher for incoming emails
    """
    def __init__(self):
        self.emailArrived = Event()

    def triggerEmail(self, message):
        """
        Trigger function for the event.
        """
        self.emailArrived(message)

