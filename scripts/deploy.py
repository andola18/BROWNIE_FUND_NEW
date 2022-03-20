from brownie import FundMe, MockV3Aggregator, network, config
from scripts.get_account_code import get_account 
def dep():

    account = get_account()
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()]["eth-usd-price-feed"]
    else:
        mock_variable = MockV3Aggregator.deploy(18, 200000000, {"from": account})
        price_feed_address = mock_variable.address
    fund_me = FundMe.deploy(price_feed_address, {"from": account})
    print(f"contract deployed at {fund_me.address}")
    #print(f"contract deployed at {fund_me.address}")
def main():
    dep()