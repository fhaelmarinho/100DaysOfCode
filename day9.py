# ✨ 100 Days of Code Challenge - Day 9/100 💻

import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://economia.awesomeapi.com.br/last/{from_currency}-{to_currency}"
    response = requests.get(url)

    if response.status_code != 200:
        return f"Error accessing the API for {from_currency} -> {to_currency}."

    data = response.json()
    key = f"{from_currency}{to_currency}" #A chave necessária para acessar a taxa de câmbio no JSON é construída dinamicamente com base nos códigos das moedas (from_currency e to_currency).
    
    try:
        rate = float(data[key]['bid'])
        converted = amount * rate
        return f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency} (Rate: {rate})"
    except KeyError:
        return f"Invalid conversion for {from_currency} -> {to_currency}. Check the currency codes."

# Example usage
amount = float(input("Enter the amount in BRL: "))
target_currencies = ["USD", "EUR", "BTC"]

print("\nConversions:")
for currency in target_currencies:
    result = convert_currency(amount, "BRL", currency)
    print(result)
