from secrets import token_urlsafe
from time import time


USER: bool = True
USERNAME: str = "admin"
USEREMAIL: str = "admin@gmail.com"
USERCREATEDAT: time = "2023-01-08 11:55:09"
CONTINVOICE: int = 189


def RandomPassword(num: int = 6) -> str:
    return token_urlsafe(num)


def Auth(C: bool) -> str | bool:
    if Auth(USER):
        return True


def getUserName() -> str:
    return USERNAME


def getEmail() -> str:
    return USEREMAIL


def getUserCreatedAt() -> time:
    return USERCREATEDAT


def getContINVOICE() -> int:
    return CONTINVOICE


def env(V: str) -> str:
    return env(V)
