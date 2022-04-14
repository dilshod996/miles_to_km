import socket

hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)

print(ipaddr)