"""
aiosmtplib
==========

An asyncio SMTP client.

Originally based on smtplib from the Python 3 standard library by:
The Dragon De Monsyne <dragondm@integral.org>

Author: Cole Maclean <hi@cole.io>
"""
from .api import send
from .errors import (
    SMTPAuthenticationError,
    SMTPConnectError,
    SMTPConnectTimeoutError,
    SMTPDataError,
    SMTPException,
    SMTPHeloError,
    SMTPNotSupported,
    SMTPReadTimeoutError,
    SMTPRecipientRefused,
    SMTPRecipientsRefused,
    SMTPResponseException,
    SMTPSenderRefused,
    SMTPServerDisconnected,
    SMTPTimeoutError,
)
from .response import SMTPResponse
from .smtp import SMTP
from .status import SMTPStatus


__title__ = "aiosmtplib"
__version__ = "1.1.1a0"
__author__ = "Cole Maclean"
__license__ = "MIT"
__copyright__ = "Copyright 2019 Cole Maclean"
__all__ = (
    "send",
    "SMTP",
    "SMTPResponse",
    "SMTPStatus",
    "SMTPAuthenticationError",
    "SMTPConnectError",
    "SMTPDataError",
    "SMTPException",
    "SMTPHeloError",
    "SMTPNotSupported",
    "SMTPRecipientRefused",
    "SMTPRecipientsRefused",
    "SMTPResponseException",
    "SMTPSenderRefused",
    "SMTPServerDisconnected",
    "SMTPTimeoutError",
    "SMTPConnectTimeoutError",
    "SMTPReadTimeoutError",
)
