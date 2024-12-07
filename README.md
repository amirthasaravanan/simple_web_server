# EX01 Developing a Simple Webserver

# Date:
# AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

# DESIGN STEPS:
## Step 1:
HTML content creation.

## Step 2:
Design of webserver workflow.

## Step 3:
Implementation using Python code.

## Step 4:
Serving the HTML pages.

## Step 5:
Testing the webserver.

# PROGRAM:
from http.server import HTTPServer,BaseHTTPRequestHandler
```
content='''
<!doctype html>
<html>
<head>
<title> My laptop configurationr</title>
</head>
<body align="center"><h1>My laptop configuration</h1>
<table border="5" align="center">
    <tr>
        <th>
            laptop configuration
        </th>
        <th>
            description
        </th>
    <tr>
        <td>
            device name
        </td>
        <td>
            LAPTOP-5JU1LOO5
        </td>
    </tr>
    <tr>
        <td>processor
        </td>
        <td>12th Gen Intel(R) Core(TM) i5-1235U   1.30 GHz
        </td>
    <tr>
        <td>Installed RAM
        </td>
        <td>
            16.0 GB (15.7 GB usable)
        </td>
    </tr>
    <tr>
        <td>
            Device ID
        </td>
        <td>
            13CCFA21-805B-4552-B107-ACD99522EF55
        </td>
    </tr>
    <tr>
        <td>
            Product ID
        </td>
        <td>00342-42684-23673-AAOEM</td>
    </tr>
    <tr>
        <td>
            System Type
        </td>
        <td>64-bit operating system, x64-based processor</td>
    </tr>
</table>
</body>
</html>
'''
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()

```
# OUTPUT:
![alt text](<Screenshot 2024-12-07 224154.png>)
![alt text](<Screenshot 2024-12-07 231822.png>)
# RESULT:
The program for implementing simple webserver is executed successfully.
