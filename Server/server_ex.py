import socket

host = ''
port = 526
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print('server is ready')
client, addr = s.accept()
print('connected by ', addr)
while True:
    data = client.recv(1024)
    if not data: break
    print('received data')
    print(data)
    client.send(b'Jieun')
    print('send data')
client.close()
s.close()