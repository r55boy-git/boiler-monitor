import socket

ip = "192.168.0.137"
port = 502

print("Connecting...")

sock = socket.create_connection((ip, port), timeout=5)

print("Connected!")

sock.close()

print("Closed.")