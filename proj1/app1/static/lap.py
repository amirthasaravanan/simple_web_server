from http.server import HTTPServer,BaseHTTPRequestHandler
'''
content=
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
            DESKTOP-MOHHBTU
        </td>
    </tr>
    <tr>
        <td>processor
        </td>
        <td>13 Gen Intel(R) Core(TM) i5-335   1.30 GHz
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
           " 15EEA3B2-7EF5-4DEC-903D-577382C3C005"
        </td>
    </tr>
    <tr>
        <td>
            Product ID
        </td>
        <td>00-42709-0-AAOEM</td>
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