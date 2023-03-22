from brownie import accounts
import os


def get_account(account_index: int):
    _private_key = os.getenv(f"PRIVATE_KEY{account_index}")
    return accounts.add(_private_key)
