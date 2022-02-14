import socket 

class Socket():

    def __init__(self):
        try:
            self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Socket successfully created")
        except socket.error as err:
            print("Socket creation failed with error %s" %(err))
            raise Exception

    def connect(self, host, port):
        try:
            self.host = host
            self.host_ip = socket.gethostbyname(host)
            self.my_socket.connect((self.host_ip, port))
            print("The socket has successfully connected\n\r")
        except socket.gaierror:
            print("There was an error resolving the host")
        except Exception as exception:
            print("There was an error connecting to the host")

    def send_request(self, asset):
        try:
            self.request = bytes("GET {asset} HTTP/1.1\r\nHost:{host}\r\n\r\n".format(asset=asset, host=self.host), 'utf-8')
            self.my_socket.settimeout(1)
            self.my_socket.sendall(self.request)
            self.response = b''
            try:
                while True:
                    self.response = self.response + self.my_socket.recv(4096);
            except socket.timeout as e:
                pass
            return self.response
        except Exception as exception:
            print("There was an error during the http request")
