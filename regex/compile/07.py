# compile/07.py
import re

# Использование re.VERBOSE

r = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # код телефона
    (\s|-|\.)?  # разделитель
    \d{3}  # первые 3 цифры номера
    (\s|-|\.)?  # разделитель
    \d{2}  # вторые 2 цифры номера
    (\s|-|\.)?  # разделитель
    \d{2})''', re.VERBOSE)  # последние 2 цифры номера


pattern = re.compile(r"\s*(?P<header>[^:]+)\s*:(?P<value>.*?)\s*$")

# вы можете также помещать внутрь РВ комментарии, длящиеся с символа # до следующей строки. 

pattern = re.compile(r"""
 \s*                 # Skip leading whitespace
 (?P<header>[^:]+)   # Header name
 \s* :               # Whitespace, and a colon
 (?P<value>.*?)      # The header's value -- *? used to
                     # lose the following trailing whitespace
 \s*$                # Trailing whitespace to end-of-line
""", re.VERBOSE)


