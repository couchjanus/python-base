from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8000

# This class will handles any incoming request from the browser 
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
	
	# Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write(b"<h1>Hello, world!</h1>")
		return

try:
	# Create a web server and define the handler to manage the
	# incoming request

	httpd = HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)

	print('Started httpserver on port ' , PORT)
	# Wait forever for incoming htto requests
	httpd.serve_forever()

except KeyboardInterrupt:
	print('^C received, shutting down the web server')
	server.socket.close()

# Run it by typing: python httpd04.py
# Then open your web browser on this URL: http://127.0.0.1:8000