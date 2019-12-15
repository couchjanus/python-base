# Example with SSL support
from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl


httpd = HTTPServer(('localhost', 4443), BaseHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile="key.pem", 
        certfile='cert.pem', server_side=True)

httpd.serve_forever()


# To generate key and cert files with OpenSSL use following command

# openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365

# import http.server
# import socketserver

# PORT = 8000

# Handler = http.server.SimpleHTTPRequestHandler

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()

# from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

# PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write("Hello World !")
		return

# try:
# 	#Create a web server and define the handler to manage the
# 	#incoming request
# 	server = HTTPServer(('', PORT_NUMBER), myHandler)
# 	print('Started httpserver on port ' , PORT_NUMBER)
	
# 	#Wait forever for incoming htto requests
# 	server.serve_forever()

# except KeyboardInterrupt:
# 	print('^C received, shutting down the web server')
# 	server.socket.close()
	

# Run it by typing:

# debarm:~/playground/python/httpserver# python example1.py

# Then open your web browser on this URL: http://fox_ip_address:8080.