import socket

host = 'localhost'
port = 19290
size = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(host, port)

try:
    # Send data
    message = 'Testing, one, two, three'
    print 'sending "%s"' % message
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print  'received "%s"' % data
finally:
    print  'closing socket'
    sock.close()
