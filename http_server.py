from http.server import HTTPServer, BaseHTTPRequestHandler    # built-in function provide basic web server and BaseHTTPRequestHandler for understand http request. 
import ssl                                                    #without this the server just http type.

class MyHandler(BaseHTTPRequestHandler):               #use this class when a request make 

    def do_GET(self):                                  #get request and tell what to do
        self.send_response(200)                        #ok,request succeed         
        self.send_header("Content-Type", "text/plain")  #how much data have to read
        self.end_headers()
        self.wfile.write(b"Hello Secure World!")        #out put in the server page


server_address = ('localhost', 4443)
httpd = HTTPServer(server_address, MyHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)                      #ssl parts..
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Serving on https://localhost:4443")

httpd.serve_forever()