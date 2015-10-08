__author__ = 'ren'
import account
import VPSign

error_mapping = {
    "LOGIN_NEEDED": (1, "login needed"),
    "USER_NT_EX": (2, "user is not exist"),
    "PW_ERROR": (3, "password error"),
    "PW_NOT_MATCH": (4, "password not match"),
    }