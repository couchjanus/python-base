# Сервер TCP srv03_recv.py

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
            # Для чтения данных используется функция recv, которой первым параметром нужно передать количество получаемых байт данных. Если столько байт, сколько указано, не пришло, а какие-то данные уже появились, она всё равно возвращает всё, что имеется, поэтому надо контролировать размер полученных данных.
            data = conn.recv(1024)
            # Тип возвращаемых данных — bytes. У этого типа есть почти все методы, что и у строк
            if not data:
                break
            # conn.sendall(data)
            # для того, чтобы использовать из него текстовые данные с другими строками (складывать, например, или искать строку в данных, или печатать), придётся декодировать данные (или их часть, если вы обработали байты и выделили строку) и использовать уже полученную строку. (Здесь и далее используется кодировка utf-8, если вы вдруг по какой-то глупости используете другую кодировку — указывайте свою.)
            print("Data: " + data.decode("utf-8"))

# Если вы попытаетесь использовать байты вместо строк, вы получите ошибку:

# >>> print("Data: "+data)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: Can't convert 'bytes' object to str implicitly

# Подключиться к серверу:

# telnet 127.0.0.1 53000
# Trying 127.0.0.1...
# Connected to 127.0.0.1.
# Escape character is '^]'.
# hello


# 
# Connected by:  ('127.0.0.1', 54092)
# IP-адрес:  127.0.0.1
# TCP порт:  54092
# Data: hello



