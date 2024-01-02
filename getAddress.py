import dune
import getBalance
import univ2calculatePrice

price_get_weth = univ2calculatePrice.get_WETH("0xc0200b1c6598a996a339196259ffdc30c1f44339")

json_data = dune.get_profit()
for row in json_data:
    tx_from = row['tx_from']
    profit = row['profit']
    balanceof_address = getBalance.balanceof_address(tx_from)
    if balanceof_address!=0:
        profit+=price_get_weth*balanceof_address

sorted_data = sorted(json_data, key=lambda x: x['profit'], reverse=True)
top_ten_addresses = []
for row in sorted_data[:10]:
    top_ten_addresses.append(row['tx_from'])
print(top_ten_addresses)
