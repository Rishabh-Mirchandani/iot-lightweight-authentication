import socket
import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
public_key = key.publickey().export_key()

HOST = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

conn, addr = server.accept()

start_time = time.time()

conn.send(public_key)
encrypted_nonce = conn.recv(256)

cipher = PKCS1_OAEP.new(key)
cipher.decrypt(encrypted_nonce)

end_time = time.time()
print("[RSA SERVER] Latency:", end_time - start_time)

conn.send(b"VERIFIED")
conn.close()
server.close()
