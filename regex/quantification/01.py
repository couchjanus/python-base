# 01.py
import re

# Finding All Instances
text = "I want to buy a mobile between 200 and 400 euros"

# We want to search all the digits from this string. If we use the search function, only the first occurrence of digits i.e. 200 will be returned as shown below:

result = re.search(r"\d+", text)
print(result.group(0))

# On the other hand, the findall function returns a list that contains all the matched utterances as shown below:

text = "I want to buy a mobile between 200 and 400 euros"
result = re.findall(r"\d+", text)
print(result)
