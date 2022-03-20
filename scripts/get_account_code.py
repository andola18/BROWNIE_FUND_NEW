from brownie import accounts, config, network
def get_account():
    if (network.show_active() == "development" or network.show_active() == "mainnet-fork"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])