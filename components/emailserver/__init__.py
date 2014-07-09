__author__ = 'haukurk'

from .server import CustomSMTPServer

smtp_server = CustomSMTPServer(('0.0.0.0', 25), None)