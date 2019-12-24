# findall 01.py
import re

# Поиск слова
pattern = 'it'

text = """I once had a big fat cat
    Who caught a big friendly rat.
    She played with it like a toy
    It gave her so much joy
    That she spared it and that was that.
    """

for match in re.findall(pattern, text):
    print('Found {!r}'.format(match))

# Подсчитать количество слов it в строке.
found = re.findall(pattern, text)

print(f'Found {len(found)} words {pattern}')

# len(found) == text.count('it')
