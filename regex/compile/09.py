# compile/09.py
import re

# Код цвета

def check_color(s):
    regex = re.compile(r"\#([a-fA-F]|[0-9]){3,6}")
    if regex.match(s):
        return True
    return False

color = "#FFFFFF"
print(check_color(color))
