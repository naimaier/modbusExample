from pyModbusTCP.client import ModbusClient
from gearman import GearmanWorker
import json

def reader(worker, job):
    c = ModbusClient(host="localhost", port=502)

    if not c.is_open() and not c.open():
        print("unable to connect to host")

    if c.is_open():

        holdingRegisters = c.read_holding_registers(1, 4)

        # Imagine we've "energy" value in position 1 with two works
        energy = (holdingRegisters[0] << 16) | holdingRegisters[1]

        # Imagine we've "power" value in position 3 with two works
        power = (holdingRegisters[2] << 16) | holdingRegisters[3]

        out = {"energy": energy, "power": power}
        return json.dumps(out)
    return None

worker = GearmanWorker(['127.0.0.1'])

worker.register_task('modbusReader', reader)

print 'working...'
worker.work()
