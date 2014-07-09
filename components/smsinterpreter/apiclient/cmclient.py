__author__ = 'haukurk'

from .base import APIClient_CM
import config


class APIError(Exception):
    """Exceptions for the API"""

    # For reference.
    STATUS_MAP = {
        200: "200 OK: Success",
        202: "202 Accepted: Your request was accepted and the user was queued for processing.",
        401: "401 Not Authorized: either you need to provide authentication credentials, or the credentials "
             "provided aren't valid.",
        403: "403 Bad Request: your request is invalid, and we'll return an error message that tells you why. "
             "This is the status code returned if you've exceeded the rate limit (see below).",
        404: "404 Not Found: either you're requesting an invalid URI or the resource in question doesn't "
             "exist (ex: no such user in our system).",
        500: "500 Internal Server Error: we did something wrong.",
        501: "501 Not implemented.",
        502: "502 Bad Gateway: returned if ITAPI is down or being upgraded.",
        503: "503 Service Unavailable: the ITAPI servers are up, but are overloaded with requests. Try again later.",
    }

    def __init__(self, status, response=None):
        self.response = response
        self.status = status

    def __str__(self):
        return "%s (%s)" % (self.status, self.STATUS_MAP.get(self.status, 'Unknown error.'))

    def __repr__(self):
        return "%s(status=%s)" % (self.__class__.__name__, self.status)


class CMClient(APIClient_CM):
    BASE_URL = "https://secure.cm.nl/smssgateway/cm/gateway.ashx"
    API_USERNAME = config.API_USERNAME
    API_PASSWORD = config.API_PASSWORD
    API_CUSTOMER_NUMBER = config.API_CUSTOMER_NUMBER
    SMS_SENDER_NAME = config.SMS_SENDER_NAME
    SMS_TARIFF = config.SMS_TARIFF

    def _handle_response(self, response):
        if response.status > 299:
            raise APIError(response.status, response=response)

        return {'status': response.status, 'message': response.data}