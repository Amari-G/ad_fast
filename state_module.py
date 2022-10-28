import socket

sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)
sckt.bind(('', 8890))

while True:
    try:
        data, server = sckt.recvfrom(1024)
        print(data.decode())
    except Exception as error:
        print(error)
        sckt.close()
        break
