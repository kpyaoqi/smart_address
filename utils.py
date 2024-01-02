import requests
import json


# 获取智能合约 ABI
def getabi(contract_address):
    abi_url = f"https://api.etherscan.io/api?module=contract&action=getabi&address={contract_address}"
    abi_response = requests.get(abi_url)
    abi_data = abi_response.json()
    contract_abi = json.loads(abi_data['result'])
    if contract_abi:
        return contract_abi
    else:
        print("Error: Unable to fetch contract ABI")


def get_ethereum_price():
    api_url = 'https://api.coingecko.com/api/v3/simple/price'
    # Parameters for Ethereum
    params = {
        'ids': 'ethereum',
        'vs_currencies': 'usd'
    }
    try:
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            data = response.json()
            ethereum_price = data['ethereum']['usd']
            return ethereum_price
        else:
            print(f"Error: Unable to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
