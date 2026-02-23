1. Import modules

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
```

 `HTTPServer` → creates the web server
 `BaseHTTPRequestHandler` → handles HTTP requests (GET, POST)
 `ssl` → Built-in module for TLS/SSL encryption,Converts normal HTTP into HTTPS.
 
2. Create Request Handler

```python
class MyHandler(BaseHTTPRequestHandler):
```
create a custom class to define how the server responds.

3. Handle GET request

```python
def do_GET(self):
```
This runs when browser sends:
```
GET /
```
Inside it:
```python
self.send_response(200)
```
→ Sends status code (200 = OK)


```python
self.send_header("Content-Type", "text/plain")
```
→ Tells browser data type

```python
self.end_headers()
```
→ Ends headers

```python
self.wfile.write(b"Hello Secure World!")
```
→ Sends response text to browser


 4. Create Server

```python
server_address = ('localhost', 4443)
httpd = HTTPServer(server_address, MyHandler)
```

 `localhost` → runs on my computer
 `4443` → port number
 `HTTPServer` → starts listening for requests


 5. Enable HTTPS

```python
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
```

* Loads certificate and private key
* Prepares encryption settings

```python
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
```
→ Converts normal HTTP into HTTPS (adds TLS encryption)


6. Start Server

```python
httpd.serve_forever()
```

→ Keeps server running and waiting for requests.

To sum up:
1. Create server
2. Define what to send when user visits
3. Load certificate
4. Add encryption
5. Start server




HTTP status codes are grouped in 5 categories:

🔵 1xx – Informational
Request received, continuing process.

 100 Continu – Server received headers, client should proceed.
 101 Switching Protocols – Protocol change (e.g., HTTP → WebSocket).


🟢 2xx – Success

The request was successfully received and processed.

200 OK** – Request succeeded (most common).
201 Created** – Resource successfully created (often after POST).
202 Accepted** – Request accepted but not yet processed.
204 No Content** – Success, but nothing to return.

🟡 3xx – Redirection

Further action is needed.

301 Moved Permanently** – URL permanently changed.
302 Found** – Temporary redirect.
304 Not Modified** – Cached version can be used.
307 Temporary Redirect** – Temporary redirect (method unchanged).
308 Permanent Redirect** – Permanent redirect (method unchanged).

🔴 4xx – Client Errors

Problem with the request.

400 Bad Request** – Malformed request.
401 Unauthorized** – Authentication required.
403 Forbidden** – Access denied.
404 Not Found** – Resource doesn’t exist.
405 Method Not Allowed** – HTTP method not supported.
408 Request Timeout** – Request took too long.
409 Conflict** – Request conflicts with server state.
429 Too Many Requests** – Rate limit exceeded.

⚫ 5xx – Server Errors

Server failed to fulfill a valid request.

500 Internal Server Error** – Generic server error.
501 Not Implemented** – Server doesn’t support functionality.
502 Bad Gateway** – Invalid response from upstream server.
503 Service Unavailable** – Server temporarily overloaded/down.
504 Gateway Timeout** – Upstream server timed out.



