import socket

# Crearting an object
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establishing a connection
# Connecting to the actual webiste or webpage to receive data
my_socket.connect(('data.pr4e.org', 80))

# The actual command to get the relevant response
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

# Sending the GET request
my_socket.send(cmd)

while True:
    # Receive upto 512 characters
    data = my_socket.recv(512)
    if (len(data) < 1):
        break

    print(data.decode())

my_socket.close()
