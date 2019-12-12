# Сервер TCP srv04_send.py
# обмен данными в TCP-соединении с помощью функций recv и send.

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 53000        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print('Connected by: ', addr)
        print('IP-адрес: ', addr[0])
        print('TCP порт: ', addr[1])
        while True:
            # Пока клиент не отключился, читаем передаваемые
            # им данные и отправляем их обратно
            data = conn.recv(1024)
            if not data:
                # Клиент отключился
                break
            # Для отправки данных в сокет используется функция send. 
            conn.send(b"Your data: " + data)
            # conn.sendall(data)
