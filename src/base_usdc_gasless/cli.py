"""Command-line entry point for the Base USDC example."""

import argparse
import json
import os

from .transfer import GaslessTransfer


def main() -> None:
    """Parse arguments, sign authorization, and print safe JSON output."""
    parser = argparse.ArgumentParser(description="Create an EIP-3009 USDC authorization")
    parser.add_argument("--rpc-url", default=os.getenv("BASE_RPC_URL", "https://mainnet.base.org"))
    parser.add_argument("--token", required=True, help="USDC contract address")
    parser.add_argument("--recipient", required=True)
    parser.add_argument("--amount", required=True, type=int, help="USDC base units (6 decimals)")
    parser.add_argument("--private-key", default=os.getenv("OWNER_PRIVATE_KEY"), required=False)
    parser.add_argument("--chain-id", type=int, default=8453)
    args = parser.parse_args()
    if not args.private_key:
        parser.error("--private-key or OWNER_PRIVATE_KEY is required")
    transfer = GaslessTransfer(args.rpc_url, args.token, args.chain_id)
    authorization = transfer.sign(args.private_key, args.recipient, args.amount)
    print(json.dumps({"owner": authorization.owner, "recipient": authorization.recipient, "value": authorization.value, "validAfter": authorization.valid_after, "validBefore": authorization.valid_before, "nonce": authorization.nonce.hex(), "v": authorization.v, "r": authorization.r.hex(), "s": authorization.s}, indent=2))


if __name__ == "__main__":
    main()
