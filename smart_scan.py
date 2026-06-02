from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient(
    "192.168.0.137",
    port=502,
    timeout=5
)

if not client.connect():
    print("Failed to connect")
    exit()

print("Connected\n")

for start in range(0, 200, 20):

    try:
        result = client.read_holding_registers(
            address=start,
            count=20
        )

        if result.isError():
            continue

        interesting = False

        for i, value in enumerate(result.registers):
            if value != 0:
                interesting = True

        if interesting:

            print(f"Registers {start}-{start+19}")

            for i, value in enumerate(result.registers):

                register = start + i

                if value != 0:

                    if 100 <= value <= 1000:
                        print(
                            f"  R{register:03}: {value:5}  ({value/10:.1f}?)"
                        )
                    else:
                        print(
                            f"  R{register:03}: {value:5}"
                        )

            print()

    except Exception as e:
        print(f"Error at {start}: {e}")

client.close()