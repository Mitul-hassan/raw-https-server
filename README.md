HTTP status codes are grouped into **5 categories**:

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



