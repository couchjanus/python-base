from http.server import HTTPServer, BaseHTTPRequestHandler
from os import curdir, sep

PORT = 8000

# This class will handles any incoming request from the browser 
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
	
	# Handler for the GET requests
	
	def do_GET(self):
		if self.path=="/":
			self.path="/index.html"

		try:
			# Check the file extension required and
			# set the right mime type

			sendReply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
				# Open the static file requested and send it
				f = open(curdir + sep + self.path, 'rb') 
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			return


		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)


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


# Run it by typing: python httpd05.py
# Then open your web browser on this URL: http://127.0.0.1:8000