from brownie import GSToken, network
from scripts.reusables import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000000, "ether")

def main():
    account = get_account()
    token = GSToken.deploy(initial_supply, {"from": account})
    # print(token.balanceOf(account))
    # print(token.totalSupply())
    # print(account)
