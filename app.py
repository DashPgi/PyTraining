
import requests

API_KEY = "575310d0056b4736b19f40c4ccff12c1"

URL = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}"


def get_rates():
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()

    print("پایه ارز (Base):", data["base"])
    print("زمان به‌روزرسانی:", data["timestamp"])
    print("-" * 40)


    important_currencies = ["EUR", "GBP", "IRR", "JPY", "CNY", "AED", "TRY"]
    for currency in important_currencies:
        if currency in data["rates"]:
            print(f"{currency}: {data['rates'][currency]}")

    return data["rates"]


def get_specific_rate(target_currency, all_rates):

    if target_currency in all_rates:
        return all_rates[target_currency]
    else:
        print(f"Arz {target_currency} پیدا نشد.")
        return None


if __name__ == "__main__":
    rates = get_rates()


    eur_rate = get_specific_rate("EUR", rates)
