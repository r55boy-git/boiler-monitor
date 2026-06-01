from pymodbus.client import ModbusTcpClient

ip = "192.168.0.137"

print("Starting...")

client = ModbusTcpClient(
    ip,
    port=502,
    timeout=5
)

print("Attempting connection...")

connected = client.connect()

print("Connected:", connected)

client.close()

print("Finished.")