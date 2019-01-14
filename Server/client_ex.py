import socket

host=socket.gethostname()
port=526
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
print('connected')

client.send(b'Yeeun')
print('send data')
data = client.recv(1024)
print('receive data')
print(data)

client.close()
