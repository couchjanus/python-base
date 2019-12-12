# Сервер TCP srv02_accept.py

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 53000        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0) as s:
    s.bind((HOST, PORT))
    s.listen()
    # принимаем соединения с помощью функции accept. Она ждёт появление входящего соединения и возвращает связанный с ним сокет и адрес подключившегося. Адрес — массив, состоящий из IP-адреса и порта.
    conn, addr = s.accept()
    # В объекте conn теперь у нас сокет, через который мы можем обмениваться данными с клиентом, в addr[0] — IP-адрес подключившегося клиента. Чтобы получить следующего клиента, нужно вызвать функцию accept ещё раз, при этом необязательно закрывать соединение с предыдущим клиентом: соединений может быть условно неограниченное количество.

    with conn:
        print('Connected by: ', addr)
        print('IP-адрес: ', addr[0])
        print('TCP порт: ', addr[1])

# Подключиться к этому серверу можно с использованием консольной утилиты telnet, предназначенной для текстового обмена информацией поверх протокола TCP:

# telnet 127.0.0.1 53000
# Trying 127.0.0.1...
# Connected to 127.0.0.1.
# Escape character is '^]'.
# Connection closed by foreign host.

# Connected by ('127.0.0.1', 53976)

# Каждый TCP сокет определяется двумя парами чисел: (локальный IP адрес, локальный порт) и (удаленный IP адрес, удаленный порт). Рассмотрим, какие адреса на данный момент у наших сокетов:

# serv_sock:
#   laddr (ip=<server_ip>, port=53000)
#   raddr (ip=0.0.0.0, port=*)  # т.е. любой

# client_sock:
#   laddr (ip=<client_ip>, port=54028)  # случайный порт, назначенный системой
#   raddr (ip=<server_ip>, port=53000)  # адрес слушающего сокета на сервере

# Connected by:  ('127.0.0.1', 54028)
# IP-адрес:  127.0.0.1
# TCP порт:  54028
