import subprocess
import time

TRIALS = 10

rsa_latencies = []
hmac_latencies = []

print("Running RSA trials...")
for _ in range(TRIALS):
    server = subprocess.Popen(["python", "server/rsa_server.py"])
    time.sleep(1)

    start = time.time()
    subprocess.run(["python", "client/rsa_client.py"],
                   stdout=subprocess.DEVNULL)
    end = time.time()

    rsa_latencies.append(end - start)
    server.terminate()
    time.sleep(1)

print("\nRunning HMAC trials...")
for _ in range(TRIALS):
    server = subprocess.Popen(["python", "server/hmac_server.py"])
    time.sleep(0.5)

    start = time.time()
    subprocess.run(["python", "client/hmac_client.py"],
                   stdout=subprocess.DEVNULL)
    end = time.time()

    hmac_latencies.append(end - start)
    server.terminate()
    time.sleep(0.5)

print("\nRSA Latencies:", rsa_latencies)
print("HMAC Latencies:", hmac_latencies)

print("\nAverage RSA Latency:", sum(rsa_latencies)/TRIALS)
print("Average HMAC Latency:", sum(hmac_latencies)/TRIALS)
