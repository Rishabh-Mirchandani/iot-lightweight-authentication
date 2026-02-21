import matplotlib.pyplot as plt

# Experimental results (from Day 6)
protocols = ["RSA", "HMAC"]
latency = [0.92, 0.004]        # seconds
message_size = [256, 90]      # bytes

# ---- Latency Comparison ----
plt.figure()
plt.bar(protocols, latency)
plt.title("Authentication Latency Comparison")
plt.ylabel("Latency (seconds)")
plt.xlabel("Protocol")
plt.savefig("graphs/latency_comparison.png")
plt.close()

# ---- Message Size Comparison ----
plt.figure()
plt.bar(protocols, message_size)
plt.title("Authentication Message Size Comparison")
plt.ylabel("Message Size (bytes)")
plt.xlabel("Protocol")
plt.savefig("graphs/message_size_comparison.png")
plt.close()

print("Graphs generated successfully.")
