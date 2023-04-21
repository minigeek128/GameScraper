from http.server import HTTPServer, BaseHTTPRequestHandler
from database import browse

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        mySearch=browse("http://www.github.com/")
        print(mySearch.name)
        try:
            with open('templates/index.html', 'r') as f:
                content = f.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(content, 'utf8'))
        except:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404: File not found')

httpd = HTTPServer(('', 8000), MyHandler)
httpd.serve_forever()
