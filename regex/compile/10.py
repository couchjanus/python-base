# compile/10.py
import re

# Проверка адреса электронной почты

def check_email(s):
    regex = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+.+.[a-zA-Z]{2,4}")
    if regex.match(s):
        return True
    return False

email = "cat@my.cat"
print(check_email(email))
