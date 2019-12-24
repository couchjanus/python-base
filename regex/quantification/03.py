# check password 03.py
import re

def check_password(s):
    if not 6 <= len(s) <= 15:
        return False
    if not 'A' <= s[0] <= 'Z':
        return False
    if not 'a' <= s[-1] <= 'z':
        return False
    for c in s[1:-1]:
        if not ('a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9'):
            return False
    return True

def check_password_with_regexp(s):
    if re.match(r"^[A-Z]{1}[a-zA-Z0-9]{4,13}[a-z]{1}$", s):
        return True
    return False

password = "Password123"

print(check_password(password))

print(check_password_with_regexp(password))