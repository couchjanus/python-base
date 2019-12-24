# compile/06.py
import re

# Использование re.VERBOSE

def check_name(name):
	pattern = re.compile(r"^[ a-zA-Z']+$",re.VERBOSE)
	if re.match(pattern, name):
		return True
	else:
		return False

def check_email(email):
    # pattern = re.compile(r"^[a-z.-]+@[a-z.-]+$",re.VERBOSE)
    pattern = re.compile(r'''^
        [a-z.-]+
        @
        [a-z.-]+
        $''',
        re.VERBOSE)
    if re.match(pattern, email):
        return True
    else:
        return False

# Check for vaild Unix username 
name = 'user'
print(check_name(name))

# Check for vaild Unix email 
email = 'user.tom-cat@my.cat'
print(check_email(email))
