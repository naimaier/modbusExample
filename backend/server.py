#!/usr/bin/env python

from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.server.async import StartTcpServer
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

hrData = [1, 1170, 2, 1170]
store = ModbusSlaveContext(hr=ModbusSequentialDataBlock(2, hrData))

context = ModbusServerContext(slaves=store, single=True)

StartTcpServer(context)
