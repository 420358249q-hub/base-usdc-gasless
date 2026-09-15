# Base USDC gasless transfer example

This example signs an EIP-3009 `TransferWithAuthorization` payload with the token owner's key. A separate relayer can submit the resulting call and pay gas. Tests never contact an RPC endpoint and no broadcast occurs unless the caller explicitly invokes `broadcast`.

## Local verification

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e '.[test]'
.venv/bin/python -m pytest
```

## Signing

Use USDC base units (6 decimals) and keep the owner key in an environment variable or a secret manager:

```bash
# Base Mainnet USDC: 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913 (chainId: 8453)
# Base Sepolia USDC: 0x036CbD53842c5426634e7929541eC2318f3dCF7e (chainId: 84532)
OWNER_PRIVATE_KEY=0x... \
.venv/bin/base-usdc-transfer \
  --token 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913 \
  --recipient 0x... \
  --amount 1000000 \
  --chain-id 8453
```

The CLI prints only the authorization fields. Review the recipient, amount, validity window, token domain, and chain ID before any relayer broadcasts the transaction.
