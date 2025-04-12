import requests

res = requests.get("https://api.delta.exchange/v2/products")
products = res.json()['result']

print("📦 Available Delta Symbols:")
for prod in products:
    print(f"{prod['symbol']} → ID: {prod['id']}")
