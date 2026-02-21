import socket
import hmac
import hashlib
import time

DEVICE_KEYS = {"device01": b"super_secret_key"}

HOST = "127.0.0.1"
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

conn, addr = server.accept()
start_time = time.time()

data = conn.recv(1024).decode()
device_id, timestamp, recv_hmac = data.split("|")

secret = DEVICE_KEYS[device_id]
msg = (device_id + timestamp).encode()
expected = hmac.new(secret, msg, hashlib.sha256).hexdigest()

end_time = time.time()
print("[HMAC SERVER] Latency:", end_time - start_time)

if hmac.compare_digest(expected, recv_hmac):
    conn.send(b"VERIFIED")
else:
    conn.send(b"FAILED")

conn.close()
server.close()
