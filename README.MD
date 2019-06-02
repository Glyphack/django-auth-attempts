# What is this?
This project is a simple django app that authorize users using phone_number instead of username
(no sms services enabled) and if user fails on login user will be restricted to login.

## simple usage log
```
 :~$ http post http://127.0.0.1:8000/api-t-auth/ username=+98123456789 password=123qwe
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 52
Content-Type: application/json
Date: Sun, 02 Jun 2019 06:39:45 GMT
Server: WSGIServer/0.2 CPython/3.6.8
X-Frame-Options: SAMEORIGIN

{
    "token": "f4cd593c8cb0f1396c44bcc9387d498d044c73a4"
}

 :~$ http post http://127.0.0.1:8000/api-t-auth/ username=+9812345678 password=123qwe
HTTP/1.1 403 Forbidden
Allow: POST, OPTIONS
Content-Length: 39
Content-Type: application/json
Date: Sun, 02 Jun 2019 06:39:52 GMT
Server: WSGIServer/0.2 CPython/3.6.8
X-Frame-Options: SAMEORIGIN

{
    "detail": "Invalid username/password."
}

 :~$ http post http://127.0.0.1:8000/api-t-auth/ username=+9812345678 password=123qwe
HTTP/1.1 403 Forbidden
Allow: POST, OPTIONS
Content-Length: 39
Content-Type: application/json
Date: Sun, 02 Jun 2019 06:39:56 GMT
Server: WSGIServer/0.2 CPython/3.6.8
X-Frame-Options: SAMEORIGIN

{
    "detail": "Invalid username/password."
}

 :~$ http post http://127.0.0.1:8000/api-t-auth/ username=+9812345678 password=123qwe
HTTP/1.1 403 Forbidden
Allow: POST, OPTIONS
Content-Length: 39
Content-Type: application/json
Date: Sun, 02 Jun 2019 06:39:57 GMT
Server: WSGIServer/0.2 CPython/3.6.8
X-Frame-Options: SAMEORIGIN

{
    "detail": "Invalid username/password."
}

 :~$ http post http://127.0.0.1:8000/api-t-auth/ username=+9812345678 password=123qwe
HTTP/1.1 403 Forbidden
Allow: POST, OPTIONS
Content-Length: 39
Content-Type: application/json
Date: Sun, 02 Jun 2019 06:39:58 GMT
Server: WSGIServer/0.2 CPython/3.6.8
X-Frame-Options: SAMEORIGIN

{
    "detail": "Invalid username/password."
}

 :~$ http post http://127.0.0.1:8000/api-t-auth/ username=+9812345678 password=123qwe
HTTP/1.1 403 Forbidden
Allow: POST, OPTIONS
Content-Length: 39
Content-Type: application/json
Date: Sun, 02 Jun 2019 06:39:59 GMT
Server: WSGIServer/0.2 CPython/3.6.8
X-Frame-Options: SAMEORIGIN

{
    "detail": "Invalid username/password."
}

 :~$ http post http://127.0.0.1:8000/api-t-auth/ username=+9812345678 password=123qwe
HTTP/1.1 403 Forbidden
Allow: POST, OPTIONS
Content-Length: 31
Content-Type: application/json
Date: Sun, 02 Jun 2019 06:40:01 GMT
Server: WSGIServer/0.2 CPython/3.6.8
X-Frame-Options: SAMEORIGIN

{
    "detail": "you are locked out"
}

 :~$ http post http://127.0.0.1:8000/api-t-auth/ username=+981234567 password=123qwe
HTTP/1.1 403 Forbidden
Allow: POST, OPTIONS
Content-Length: 33
Content-Type: application/json
Date: Sun, 02 Jun 2019 06:40:06 GMT
Server: WSGIServer/0.2 CPython/3.6.8
X-Frame-Options: SAMEORIGIN

{
    "detail": "you're ip is blocked"
}
```