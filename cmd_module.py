import socket

sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)
sckt.bind(('', 9000))

while True:
    try:
        message = input('')

        if not message:
            break

        if 'end' in message:
            sckt.close()
            break

        message = message.encode()
        sent = sckt.sendto(message, tello_address)
    except Exception as error:
        print(error)
        sckt.close()
        break
