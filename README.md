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
OWNER_PRIVATE_KEY=0x... \
.venv/bin/base-usdc-transfer \
  --token 0xA0b86991c6218b36c1d19d4a2e9eb0ce3606eb48 \
  --recipient 0x... \
  --amount 1000000
```

The CLI prints only the authorization fields. Review the recipient, amount, validity window, token domain, and chain ID before any relayer broadcasts the transaction.
