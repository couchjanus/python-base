import socket

class NoHandlerError(Exception):
    pass

class Request:
    pass

class Handler:
    def can_handle(self, request):
        return False

    def handle(self, request):
        raise RuntimeError("abstract")

class Server:
    def __init__(self, host='127.0.0.1', port=80):
        self.s = socket.socket()
        server_addr = host, port
        self.s.bind(server_addr)
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def get(self, path):
        def decorator(f):
            class DynamicHandler(Handler):
                def can_handle(self, request):
                    return request.method == 'GET' and request.path == path
                def handle(self, request):
                    return f(request)
            self.handlers.append(DynamicHandler())
            return f
        return decorator

    def serve_forever(self):
        self.s.listen()
        while True:
            s2, client_addr = self.s.accept()
            try:
                self.handle_client(s2)
            except:
                try:
                    s2.send(b'HTTP/1.0 500 Internal Server Error\r\n\r\n')
                except:
                    pass  # the socket has died, do nothing
            finally:
                s2.close()

    def handle_client(self, socket):
        client_handler = ClientHandler(socket, self.handlers)
        request = client_handler.parse_request()
        response = client_handler.handle_request(request)
        client_handler.send_response(response)


class ClientHandler:
    def __init__(self, socket, handlers):
        self.socket = socket
        self.handlers = handlers

    def parse_request(self):
        raw_request = self.socket.recv(2048).decode().splitlines()
        request = Request()
        first_line = raw_request.pop(0)
        # METHOD /path HTTP/version
        request.method, request.path, request.http_version = first_line.split()
        request.http_version = request.http_version[len('HTTP/'):]

        request.headers = self.parse_headers(raw_request)
        request.body = '\n'.join(raw_request)

        return request

    def parse_headers(self, raw_request):
        headers = dict()
        while True:
            line = raw_request.pop(0)
            if not line:
                # reached the end of headers
                break
            name, colon, value = line.partition(': ')
            headers[name] = value
        return headers

    def handle_request(self, request):
        for handler in self.handlers:
            if handler.can_handle(request):
                return handler.handle(request)
        raise NoHandlerError()

    def send_response(self, response):
        if isinstance(response, str):
            code = 200
            body = response
        else:
            code, body = response
        body = body.encode()

        code_name = {
            200: 'OK',
            201: 'Created',
            404: 'Not Found'
        }[code]

        self.socket.send('HTTP/1.0 {} {}\r\n'.format(code, code_name).encode())

        self.send_header('Server', 'Simple HTTP server 0.1')
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(body))

        self.finish_headers()
        self.socket.send(body)

    def send_header(self, name, value):
        self.socket.send('{}: {}\r\n'.format(name, value).encode())

    def finish_headers(self):
        self.socket.send(b'\r\n')


server = Server(port=8000)

@server.get('/')
def root(request):
    return '''
        <html>
            <head>
                <title>Hello Python</title>
            </head>
            <body>
                <h1>Hello Python</h1>
            </body>
        </html>'''

server.serve_forever()
