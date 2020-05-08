import base64
import logging

from passlib.context import CryptContext
from passlib.handlers.pbkdf2 import pbkdf2_sha256

log = logging.getLogger(__name__)

pwd_context = CryptContext(schemes=['pbkdf2_sha256'], deprecated='auto')
pwd_context_verifying = pbkdf2_sha256


def string_to_base64(s):
    return base64.b64encode(s.encode('utf-8'))


def base64_to_string(b):
    return base64.b64decode(b).decode('utf-8')


def string_to_byte(s):
    return s.encode('utf-8')


def byte_to_string(s):
    return s.decode('utf-8')
