# compile/08.py
import re

# Пример создания выражения для проверки пароля:
# условия: обязательно нижний верхний регистр цифры

def check_password_with_regexp(s):
    regex = re.compile(r'.*([a-z]{1,}[A-Z]{1,}[0-9]{1,}|[A-Z]{1,}[a-z]{1,}[0-9]{1,}|[0-9]{1,}[A-Z]{1,}[a-z]{1,}|[a-z]{1,}[0-9]{1,}[A-Z]{1,}|[A-Z]{1,}[0-9]{1,}[a-z]{1,}).*')

    if regex.match(s):
        return True
    return False

password = "PWor12@a"
print(check_password_with_regexp(password))


# Надежность пароля - довольно субъективное понятие, поэтому не существует универсального решения для проверки. 

def check_password_with_regex(s):
    regex = re.compile(r'^(?=.*[A-Z].*[A-Z])(?=.*[!@#$&*])(?=.*[0-9].*[0-9])(?=.*[a-z].*[a-z].*[a-z]).{8}$')
    if regex.match(s):
        return True
    return False

password = "PWor12@a"
print(check_password_with_regex(password))
