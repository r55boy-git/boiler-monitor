from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient(
    "192.168.0.137",
    port=502,
    timeout=5
)

if not client.connect():
    print("Unable to connect")
    exit()

ambient = client.read_holding_registers(address=2, count=1).registers[0]
plant_mode = client.read_holding_registers(address=3, count=1).registers[0]
error_code = client.read_holding_registers(address=5, count=1).registers[0]
flow_temp = client.read_holding_registers(address=22, count=1).registers[0]
pump = client.read_holding_registers(address=23, count=1).registers[0]
boiler_temp = client.read_holding_registers(address=102, count=1).registers[0]
hc_state = client.read_holding_registers(address=15,count=1).registers[0]

client.close()

plant_modes = {
    0: "Off",
    1: "Auto",
    2: "Domestic Hot Water"
}
hc_states = {
    0: "Permanent Op",
    1: "Start",
    2: "Ignition",
    3: "Softstart",
    4: "Heating Full Power",
    5: "Run On Time",
    6: "Off",
    7: "Suction",
    8: "Ash",
    9: "Pellet",
    10: "Pellet Switch",
    11: "Error",
    12: "Calibration"
}
state_icons = {
    0: "🟢",
    1: "🟡",
    2: "🔥",
    3: "🔥",
    4: "🔥",
    5: "🟡",
    6: "⚫",
    7: "🔄",
    8: "🧹",
    9: "🌾",
    10: "🌾",
    11: "❌",
    12: "⚙️"
}

icon = state_icons.get(hc_state, "❓")


print()
print("🔥 BOILER STATUS")
print("----------------------")
print(f"Ambient Temp : {ambient/10:.1f} °C")
print(f"Boiler Temp  : {boiler_temp/10:.1f} °C")
print(f"Flow Temp    : {flow_temp/10:.1f} °C")
print(f"Plant Mode   : {plant_modes.get(plant_mode, plant_mode)}")
print(f"Pump Running : {'Yes' if pump else 'No'}")
print(f"Error Code   : {error_code}")
print(f"Boiler State : {icon} {hc_states.get(hc_state, f'Unknown ({hc_state})')}")
print()