Testing [asynio](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor) + [tornado](https://www.tornadoweb.org/en/stable/) for blocking ops.

```bash
python -m virtualenv venv3 -p python3 
source venv3/bin/activate
python api.py

curl localhost:1234/block 
curl localhost:1234/
```
