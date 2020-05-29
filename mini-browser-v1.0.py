import socket

my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_socket.connect(('data.pr4e.org', 80))
my_url = "Get http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode()
my_socket.send(my_url)

while True:
    data = my_socket.recv(512)
    if len(data) <1 :
        continue
    print(data.decode(),end='')

my_socket.close()