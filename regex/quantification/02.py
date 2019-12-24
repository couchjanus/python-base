# 02.py
import re

# Finding All Instances
text = "I want to buy a mobile between 200 and 400 euros"

# Extract each character

result =re.findall(r".", text)
print(result)

# To avoid space use "\w"
result =re.findall(r"\w", text)
print(result)

# Extract each word 
result =re.findall(r"^\w+", text)
print(result)

# $ returns the word from end of the string
result = re.findall(r"\w+$", text)
print(result)

# Return first two characters of each word

result = re.findall(r"\w\w", text)
print(result)

# Extract consecutive two characters at start of word boundary

result = re.findall(r"\b\w.", text)
print(result)

# Extract date
result = re.findall(r"\d", text)
print(result)

# Return words starts with alphabets
# returns list
result = re.findall(r"[aeiouAEIOU]\w+", text)
print(result)
