from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient(
    "192.168.0.137",
    port=502,
    timeout=5
)

if client.connect():

    print("Connected")

    result = client.read_holding_registers(
        address=0,
        count=10
    )

    print(result)

    client.close()

else:
    print("Failed to connect")