# findall 02.py
import re

# Необходимо найти все e-mail в заданном тексте
# Данные шаблон сильно упрощен для понимания!
# см. http://stackoverflow.com/questions/201323/
#     using-a-regular-expression-to-validate-an-email-address

EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+[a-zA-Z]"

text = """Это произвольный текст, в котором будет происходить поиск
адресов электронной почты (e-mail). Скажу сразу, что мой e-mail
ya@gmail.com; папы и мамы: papa@gmail.com и mama@gmail.com, а также брата
brat@hotmail.com и даже моего любимого кота: pushok@cat.com."""

# 1. Используя re.search() + re.finditer()
m = re.search(EMAIL_REGEX, text, re.MULTILINE)
if m:
    for item in re.finditer(EMAIL_REGEX, text):
        # 'item' - объект класса match
        print("Найден e-mail: {}, позиция {}".format(item.group(0),
                                                     item.span()))
else:
    print("Ни одного e-mail не найдено!")

# 2. Используя re.findall()
res = re.findall(EMAIL_REGEX, text, re.MULTILINE)
if len(res) > 0:
    for item in res:  # 'item' - строка
        print("Найден e-mail: {}".format(item))
else:
    print("Ни одного e-mail не найдено!")
