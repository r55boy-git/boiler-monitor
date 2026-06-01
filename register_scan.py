from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient(
    "192.168.0.137",
    port=502,
    timeout=5
)

if client.connect():

    print("Connected")
    print()

    #for address in range(0, 100, 10):
    for address in range(0, 100, 10):

        try:

            result = client.read_holding_registers(
                address=address,
                count=10
            )

            print(f"Address {address}:")
            print(result.registers)
            print()

        except Exception as e:
            print(f"Address {address}: ERROR {e}")

    client.close()