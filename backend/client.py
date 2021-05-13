from pyModbusTCP.client import ModbusClient
import json

def reader():
    c = ModbusClient(host="localhost", port=502)

    if not c.is_open() and not c.open():
        print("unable to connect to host")

    if c.is_open():

        holdingRegisters = c.read_holding_registers(1, 4)

        # Imagine we've "energy" value in position 1 with two words
        energy = (holdingRegisters[0] << 16) | holdingRegisters[1]

        # Imagine we've "power" value in position 3 with two words
        power = (holdingRegisters[2] << 16) | holdingRegisters[3]

        out = {"energy": energy, "power": power}

        print(out)
        
        return json.dumps(out)
    return None

reader()
