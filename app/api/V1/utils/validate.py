import re


def validate_username(self, name):
    regex = "[a-zA-z]{3,10}$"
    re.match(regex, name)
