import requests

def get_profit():
    api_key = 'BKaV4vEzP8xXI263hSjWG21ecEvSvuFI'
    query_id = 3252037
    url = f"https://api.dune.com/api/v1/query/{query_id}/results?api_key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        dune_data = response.json()
        return dune_data["result"]["rows"]
    else:
        # 输出错误信息
        print(f"API请求失败，状态码: {response.status_code}, 错误信息: {response.text}")
