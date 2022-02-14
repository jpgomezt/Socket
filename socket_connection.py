import socket 
import sys
 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))
 
# default port for socket
port = 80
 
try:
    host_ip = socket.gethostbyname('www-net.cs.umass.edu')
    print(host_ip)
except socket.gaierror:
    # this means could not resolve the host
    print ("there was an error resolving the host")
    sys.exit()
 
# connecting to the server
s.connect((host_ip, port))
 
print ("the socket has successfully connected")

request = b"GET /wireshark-labs/Wireshark_HTTP_v8.0.pdf HTTP/1.1\r\nHost:www.columbia.edu\r\n\r\n"
s.settimeout(1)
s.send(request)
response = b''
try:
    while True:
        response = response + s.recv(4096);
except socket.timeout as e:
    pass
httppp_header = {}
count = 0
current_header = 'Status'
read_value = ''
reading_header_value = False
tamano = len(response)

while count < len(response):
    if(response[count] == 58 and not(reading_header_value)):
        current_header = read_value
        reading_header_value = True
        read_value = ''
        count = count + 1
    elif((response[count] == 13) and (response[count+1] == 10)):
        httppp_header[current_header] = read_value
        if((response[count+2] == 13) and (response[count+3] == 10)):
            count = count + 4
            break
        reading_header_value = False
        read_value = ''
        count = count + 1
    else:
        read_value = read_value + chr(response[count])
    count = count + 1

http_body = response[count:len(response)]
print(httppp_header)
print(response[0:count])
#print(http_body)