Modbus example
==============

I assume you install frontend dependencies (via composer) and backend (via pip)

Run gearman
```
gearmand
```

Run fake modbus server (we need sudo because it opens 502 port) 
 
```
python backend/fakeServer.py
```

Run worker
 
```
python backend/worker.py
```

Start frontend server
```
php -S 0.0.0.0:8080 t frontend/www
```





