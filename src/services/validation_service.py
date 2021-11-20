from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from settings import Settings
from utils.exceptions import DecryptError, InvalidToken, ValidationError

token_scheme = OAuth2PasswordBearer("")


def check_user_token(token: str = Depends(token_scheme)):
    try:
        decrypt_token = Settings.ENCRYPTOR.decrypt(token.encode()).decode()
    except Exception:
        raise DecryptError

    if decrypt_token != Settings.SECRET_KEY:
        raise InvalidToken


def check_service_field(value):
    if value[0] != "s":
        raise ValidationError(msg="Error service name")
    if not value[1:].isdigit():
        raise ValidationError(msg="Error service number")


def check_service_value(value):
    if value not in (None, 0, 1, 2):
        raise ValidationError(msg="Error service value")
