from unittest.mock import Mock, patch

import pytest
from eth_account import Account
from web3 import Web3

from base_usdc_gasless.transfer import GaslessTransfer


KEY = "0x59c6995e998f97a5a0044976f0945389dc9e86dae88c7a9f7f7f2f8f4f4f4f4f"
TOKEN = "0xA0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"
RECIPIENT = "0x000000000000000000000000000000000000dEaD"


def test_sign_is_recoverable_and_deterministic() -> None:
    transfer = GaslessTransfer("http://127.0.0.1:8545", TOKEN, 8453)
    auth = transfer.sign(KEY, RECIPIENT, 1_000_000, valid_for_seconds=60, nonce=bytes(32), now=1_700_000_000)
    assert auth.owner == Account.from_key(KEY).address
    assert auth.valid_before == 1_700_000_060
    assert len(auth.r) == len(auth.s) == len(auth.nonce) == 32


def test_rejects_invalid_amount_and_nonce() -> None:
    transfer = GaslessTransfer("http://127.0.0.1:8545", TOKEN, 8453)
    with pytest.raises(ValueError, match="amount"):
        transfer.sign(KEY, RECIPIENT, 0)
    with pytest.raises(ValueError, match="exactly 32"):
        transfer.sign(KEY, RECIPIENT, 1, nonce=b"bad")


def test_build_transaction_uses_mock_contract() -> None:
    transfer = GaslessTransfer("http://127.0.0.1:8545", TOKEN, 8453)
    auth = transfer.sign(KEY, RECIPIENT, 1, nonce=bytes(32), now=1_700_000_000)
    fake = Mock()
    fake.functions.transferWithAuthorization.return_value.build_transaction.return_value = {"to": TOKEN, "data": "0x"}
    with patch.object(transfer.web3.eth, "contract", return_value=fake):
        tx = transfer.build_transaction(auth, Account.from_key(KEY).address, nonce=7)
    assert tx["chainId"] == 8453 and tx["nonce"] == 7 and tx["gas"] == 180_000

