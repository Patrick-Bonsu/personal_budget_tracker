import requests

def convert_currency(amount, from_currency="USD", to_currency="EUR"):
    """
    Converts amount from one currency to another using ExchangeRate.host API.
    Returns the converted amount.
    """
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("result")
    else:
        return None
