import requests

api_key = "badf9130ed30e2e908674f78"
url = f"https://v6.exchangerate-api.com/v6/{api_key}latest/USD"

response = requests.get(url)
data = response.json()
if data["result"] == "success":
    rates = data["conversion_rates"]

    print("1 USD =")
    print("Toman:", int(rates["IRR"]/10),"Toman")

else:
    print("Error:", data)