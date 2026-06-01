# Boiler Monitor

A Python-based monitoring project for an ÖkoFEN Pellematic Condens boiler.

## Goal

Read live boiler telemetry using Modbus TCP and display key information on a home touchscreen dashboard.

## Hardware

- ÖkoFEN Pellematic Condens
- Pelletronic Touch controller
- Modbus TCP enabled

## Progress

### Day 1

- Established network connectivity
- Identified boiler IP address
- Confirmed TCP port 502 open
- Connected successfully using pymodbus
- Read first Modbus holding registers
- Identified a likely temperature register

## Next Steps

- Build register map
- Identify temperatures and status values
- Create polling service
- Build dashboard UI