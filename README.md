Modbus example
==============

Install dependencies via pip:
```
pip install pymodbus==2.5.1
```
```
pip install twisted
```

Run fake modbus server (we need sudo because it opens 502 port) 
 
```
python backend/fakeServer.py
```

Run client
```
python backend/client.py
```