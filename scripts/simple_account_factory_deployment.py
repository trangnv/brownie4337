from brownie import accounts, EntryPoint, SimpleAccountFactory, config, network
from scripts.utils import get_account

entry_point_contract_address = "0x0576a174D229E3cFA37253523E645A78A0C91B57"


def main():
    deploy_simple_account_factory_contract()


def deploy_simple_account_factory_contract():
    print("Deploying SimpleAccount contract...")
    dev = get_account(0)
    simple_account_factory_contract = SimpleAccountFactory.deploy(
        entry_point_contract_address,
        {"from": dev},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    # dev1 = get_account(1)
    print(
        f"SimpleAccountFactory contract deployed at: {simple_account_factory_contract.address}"
    )
    # simple_account_factory_contract.initialize(dev1.address, {"from": dev})
    # print(f"SimpleAccount contract initialized with owner address: {dev1.address}")
