import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 50000))
s.listen(1)
conn, addr = s.accept()
while 1:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
conn.close()
