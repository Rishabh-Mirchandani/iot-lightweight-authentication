import socket
import hmac
import hashlib
import time

HOST = "127.0.0.1"
PORT = 9090

DEVICE_ID = "device01"
SECRET = b"super_secret_key"

ts = str(int(time.time()))
msg = (DEVICE_ID + ts).encode()
digest = hmac.new(SECRET, msg, hashlib.sha256).hexdigest()

payload = DEVICE_ID + "|" + ts + "|" + digest

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.send(payload.encode())
client.recv(1024)
client.close()
