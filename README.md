# Lightweight Authentication Protocols for IoT Systems

## Overview
This project presents a performance and security comparison between:
- RSA-based public-key authentication
- Lightweight HMAC-based symmetric authentication

The goal is to evaluate authentication latency and communication overhead in resource-constrained IoT environments.

## Implemented Protocols
1. RSA Challenge–Response Authentication
2. HMAC-Based Authentication with Replay Protection

## Experimental Evaluation
- 10 trials per protocol
- Measured:
  - Authentication latency
  - Message size

## Results Summary

| Protocol | Avg Latency (s) | Message Size (bytes) |
|----------|-----------------|----------------------|
| RSA      | 0.92            | 256                  |
| HMAC     | 0.004           | 90                   |

## Key Findings
- HMAC authentication significantly reduces latency.
- Symmetric-key approaches are better suited for IoT systems.
- RSA provides stronger security guarantees but at higher computational cost.

## Research Report
The full technical report is available in `report/iot_authentication_research.pdf`.