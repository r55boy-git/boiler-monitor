import socket

ip = "192.168.0.137"

ports = [
    80,
    443,
    502,    # Modbus TCP
    8080,
    8888,
    10001,
]

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((ip, port))

    if result == 0:
        print(f"OPEN: {port}")

    sock.close()