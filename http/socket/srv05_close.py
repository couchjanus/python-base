# Сервер TCP srv05_close.py
# обмен данными в TCP-соединении с помощью функций recv и send.

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 53000        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    # Если данных приходится ждать слишком долго, можно перед использованием функции recv задать (однократно) таймаут с помощью функции settimeout.
    conn.settimeout(60) # установка таймаута
    
    with conn:
        print('Connected by: ', addr)
        print('IP-адрес: ', addr[0])
        print('TCP порт: ', addr[1])
        while True:
            # В случае, если другая сторона сторона закроет сокет, функция recv вернёт пустой объект bytes.
            data = conn.recv(1024)
            # если за 60 секунд не придут никакие данные, функция recv вернёт пустой объект bytes, как и при закрытом соединении.
            if not data:
                print("No data")
                # После всего и клиенту, и серверу необходимо закрыть сокет с помощью функции close.
                conn.close() # Теперь этот сокет использовать нельзя.
            conn.send(b"Your data: " + data)
            # conn.sendall(data)

# Подключиться к серверу:

# telnet 127.0.0.1 53000
# Trying 127.0.0.1...
# Connected to 127.0.0.1.
# Escape character is '^]'.
# hello
# Your data: hello
# Connection closed by foreign host.

# Connected by:  ('127.0.0.1', 54406)
# IP-адрес:  127.0.0.1
# TCP порт:  54406
# Traceback (most recent call last):
#   File "srv05_close.py", line 22, in <module>
#     data = conn.recv(1024)
# socket.timeout: timed out
