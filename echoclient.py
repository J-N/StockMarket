import socket

host = 'localhost'
port = 19290

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
<<<<<<< HEAD

=======
size = 1024
>>>>>>> 0c851f689777b61a8589fc26cbcb7987b3fbcf12
try:
    # Send data
    message = 'Testing, one, two, three'
    print 'sending "%s"' % message
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(size)
        amount_received += len(data)
        print  'received "%s"' % data
finally:
    print  'closing socket'
    sock.close()
