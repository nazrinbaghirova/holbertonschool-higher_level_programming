Basics of HTTP/HTTPS

HTTP (Hypertext Transfer Protocol) is used for communication between a client (browser) and a server. It sends data in plain text, which means it is not secure. HTTPS (Hypertext Transfer Protocol Secure) is the secure version of HTTP. It uses SSL/TLS encryption to protect the data during transmission. Because of this, HTTPS is safer and is used for websites that handle sensitive information such as passwords or personal data. HTTP usually uses port 80, while HTTPS uses port 443.

An HTTP request contains several parts. From the Network tab observation, I saw that a request includes a method, a URL, and headers. In my case, the request method was POST and the request URL was https://f.clarity.ms/collect
. The headers contained additional information such as User-Agent, Accept, Cookie, and Host. The request may also include a body when data is sent to the server.

An HTTP response also has a structure. It includes a status code, headers, and sometimes a body. In the observed example, the status code was 204 No Content, which means the request was successful but no content was returned. The response headers included information such as server type (nginx) and date. In this case, the response body was empty.

Common HTTP methods include GET, POST, PUT, and DELETE. GET is used to retrieve data from the server, for example when opening a webpage. POST is used to send data to the server, such as submitting a form. PUT is used to update an existing resource completely, for example updating user information. DELETE is used to remove a resource from the server, such as deleting a post.

Common HTTP status codes include 200 OK, 201 Created, 204 No Content, 404 Not Found, and 500 Internal Server Error. 200 OK means the request was successful. 201 Created means a new resource was successfully created. 204 No Content means the request was successful but there is no content to return. 404 Not Found means the requested resource does not exist. 500 Internal Server Error means there is a problem on the server side.
