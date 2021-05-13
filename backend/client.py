from pymodbus.client.sync import ModbusTcpClient
import json

def reader():
    c = ModbusTcpClient(host="localhost", port=502)

    if not c.is_socket_open() and not c.connect():
        print("unable to connect to host")

    if not c.is_socket_open():
        return None

    holdingRegisters = c.read_holding_registers(1, 4)

    if holdingRegisters.isError():
        print('Error reading registers')
        return None

    # Imagine we've "energy" value in position 1 with two words
    energy = (holdingRegisters.registers[0] << 16) | holdingRegisters.registers[1]

    # Imagine we've "power" value in position 3 with two words
    power = (holdingRegisters.registers[2] << 16) | holdingRegisters.registers[3]

    out = {"energy": energy, "power": power}

    print(out)
    
    return json.dumps(out)

reader()
