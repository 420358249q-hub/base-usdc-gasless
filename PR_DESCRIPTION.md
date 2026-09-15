# Add typed Python example for Base USDC gasless transfer

## Background
Adds a small, network-independent Python example for USDC EIP-3009 `transferWithAuthorization`. The token owner signs typed data off-chain; a relayer pays gas.

## Changes
- Added `GaslessTransfer.sign` with strict validation and configurable EIP-712 domain.
- Added transaction construction and explicit opt-in broadcast helpers.
- Added CLI and mock-based unit tests; no private key or RPC call is required by tests.

## Verification
Run `python -m pytest` from this directory. Attach the CI job's green summary screenshot to the PR (include repository, commit SHA, and test count).

## Zero-Spam declaration
This PR addresses only the linked issue, contains no unrelated formatting or generated files, and does not make network calls or submit transactions during tests.
