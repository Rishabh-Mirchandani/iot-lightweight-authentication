import time
import psutil

start = time.time()
time.sleep(0.5)
end = time.time()

print("Latency:", end - start)
print("CPU Usage:", psutil.cpu_percent())
