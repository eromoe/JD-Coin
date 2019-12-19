import redis

host = '127.0.0.1'
port = 6379

client = redis.Redis(host=host, port=port)
client.set("redis", "value111", None, 1000)
print(str(client.get("redis")))
if client.get("redis1") != None and len(client.get("redis1")) > 0:
    print("sss")
else:
    print("no")


