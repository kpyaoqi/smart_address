import requests
import mysql.connector

db_config = {
    "host": "127.0.0.1",
    "port": 3307,
    "user": "root",
    "password": "root",
    "database": "biteying"
}

def get_htopair():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    url = "https://open-api.dextools.io/free/v2/ranking/ether/gainers"
    headers = {
        "X-BLOBR-KEY": "Q86h8hIBxvFv3vUjdxfdWIxVadoAK67v"
    }
    # response = {
    #     "statusCode": 200,
    #     "data": [
    #         {
    #             "rank": 1,
    #             "price": 0.00005972779539208241,
    #             "price24h": 0.000003893599368717486,
    #             "variation24h": 1433.9995139704415,
    #             "creationBlock": 18648762,
    #             "creationTime": "2023-11-25T12:38:35.000Z",
    #             "fee": 0.3,
    #             "exchange": {
    #                 "name": "Uniswap",
    #                 "factory": "0x1f98431c8ad98523631ae4a59f267346ea31f984"
    #             },
    #             "mainToken": {
    #                 "name": "BitAgo",
    #                 "symbol": "BitAgo",
    #                 "address": "0x6566a87e33e13db87a181eb9babef716b87509bc"
    #             },
    #             "sideToken": {
    #                 "name": "Wrapped Ether",
    #                 "symbol": "WETH",
    #                 "address": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
    #             }
    #         },
    #         {
    #             "rank": 2,
    #             "price": 0.00025688398336268307,
    #             "price24h": 0.00002868671616033138,
    #             "variation24h": 795.4806187189452,
    #             "creationBlock": 18661229,
    #             "creationTime": "2023-11-27T06:34:23.000Z",
    #             "fee": 0.3,
    #             "exchange": {
    #                 "name": "Uniswap",
    #                 "factory": "0x1f98431c8ad98523631ae4a59f267346ea31f984"
    #             },
    #             "mainToken": {
    #                 "name": "10000X",
    #                 "symbol": "10000X",
    #                 "address": "0x86bf94708ccde8729350c4addb745db2be3802a4"
    #             },
    #             "sideToken": {
    #                 "name": "Wrapped Ether",
    #                 "symbol": "WETH",
    #                 "address": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
    #             }
    #         }
    #     ]
    # }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
        for entry in data["data"]:
            print(entry)
            insert_query = (
                "INSERT INTO increase "
                "(id,price, price24h, variation24h, creation, exchange, factory, mainToken, mainaddress, sideToken, sideaddress) "
                "VALUES (NULL,%s, %s, %s, %s, %s,  %s, %s, %s, %s, %s)"
            )
            # Extracting values from the entry
            values = (
                entry["price"],
                entry["price24h"],
                entry["variation24h"],
                entry["creationTime"],
                entry["exchange"]["name"],
                entry["exchange"]["factory"],
                entry["mainToken"]["name"],
                entry["mainToken"]["address"],
                entry["sideToken"]["name"],
                entry["sideToken"]["address"],
            )
            cursor.execute(insert_query, values)
        conn.commit()
        cursor.close()
        conn.close()
    else:
        print(f"Error: {response.status_code}")

