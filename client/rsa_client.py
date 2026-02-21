import socket
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

HOST = "127.0.0.1"
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

public_key = client.recv(2048)
rsa_key = RSA.import_key(public_key)

cipher = PKCS1_OAEP.new(rsa_key)
nonce = os.urandom(16)
encrypted_nonce = cipher.encrypt(nonce)

client.send(encrypted_nonce)
client.recv(1024)
client.close()
