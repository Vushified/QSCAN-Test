# ECDAT E2E Test Repository

This repository contains intentionally vulnerable cryptographic code
for testing ECDAT (Enterprise Crypto Discovery and Analysis Tool).

**DO NOT USE ANY CODE IN THIS REPO IN PRODUCTION.**

## Intentional vulnerabilities:

| File | Algorithm | Vulnerability |
|------|-----------|---------------|
| python/crypto_utils.py | DES-ECB | Classically broken, 56-bit key |
| python/crypto_utils.py | MD5 | SHAttered collision attack 2004 |
| python/crypto_utils.py | RSA-2048 | Shor's algorithm (quantum) |
| python/auth_service.py | SHA-1 | SHAttered practical collision 2017 |
| java/CryptoHelper.java | DES/ECB | Classically broken |
| java/CryptoHelper.java | MD5 | SHAttered collision attack |
| java/UserAuth.java | SHA-1 | SHAttered practical collision 2017 |
| java/UserAuth.java | RSA-2048 | Shor's algorithm (quantum) |

## Expected ECDAT results:
- Total artefacts: 10-15
- Quantum vulnerable: 8+
- MIGRATE_NOW: 8+
- CDG chain: crypto_utils -> payment_service -> order_service (3-module chain)
- Migration group complexity: MEDIUM
