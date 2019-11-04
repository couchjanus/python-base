# -*- coding: utf-8 -*-
# pickle.test.py

import pickle
 
FILENAME = "users.dat"
 
users = [
    ["Tom", 28, True],
    ["Alice", 23, False],
    ["Bob", 34, False]
]
 
with open(FILENAME, "wb") as file:
    pickle.dump(users, file)
 
 
with open(FILENAME, "rb") as file:
    users_from_file = pickle.load(file)
    for user in users_from_file:
        print("Имя:", user[0], "\tВозраст:", user[1], "\tЖенат(замужем):", user[2])

# В зависимости от того, какой объект мы записывали функцией dump, 
# тот же объект будет возвращен функцией load при считывании файла.
