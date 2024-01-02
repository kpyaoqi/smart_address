from web3 import Web3
import utils

ethereum_node_url = "https://eth-mainnet.g.alchemy.com/v2/888FBdjlC2kGdFAFRKHrsCPCXdyVIbYU"
web3 = Web3(Web3.HTTPProvider(ethereum_node_url))

contract_address=web3.to_checksum_address("0xc0200b1c6598a996a339196259ffdc30c1f44339")
contract_abi = utils.getabi(contract_address)
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

def balanceof_address(user_address):
    user_address = web3.to_checksum_address(user_address)
    balance = contract.functions.balanceOf(user_address).call()
    return balance
