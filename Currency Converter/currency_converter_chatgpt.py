import requests

API_KEY = "kuSughwAaAOYxCzZbvJozxmJXnOGsV8r"
API_URL = "https://api.apilayer.com/fixer"
HEADERS = {"apikey": API_KEY}

def get_available_currencies():
    """
    Fetches the list of available currencies from the API.

    Returns:
        dict: A dictionary with currency codes as keys and currency names as values.
    """
    response = requests.get(f"{API_URL}/symbols", headers=HEADERS)
    data = response.json()
    if response.status_code != 200 or 'symbols' not in data:
        raise Exception("Error fetching currency symbols.")
    return data['symbols']

def convert_currency(from_currency, to_currency, amount):
    """
    Converts a specified amount from one currency to another using the API.

    Args:
        from_currency (str): The currency code to convert from.
        to_currency (str): The currency code to convert to.
        amount (float): The amount of currency to convert.

    Returns:
        float: The converted amount.
    """
    response = requests.get(
        f"{API_URL}/convert?to={to_currency}&from={from_currency}&amount={amount}",
        headers=HEADERS
    )
    data = response.json()
    if response.status_code != 200 or 'result' not in data:
        raise Exception("Error converting currency.")
    return data['result']

def get_currency_input(prompt, available_currencies):
    """
    Prompts the user for a currency input and ensures it's valid.

    Args:
        prompt (str): The input prompt to show the user.
        available_currencies (dict): The dictionary of available currencies.

    Returns:
        str: The valid currency code entered by the user.
    """
    while True:
        currency = input(prompt).upper()
        if currency in available_currencies:
            return currency
        print("Invalid currency code. Please try again.")

def main():
    try:
        available_currencies = get_available_currencies()
        print("Available currencies:")
        for code, name in available_currencies.items():
            print(f"{code}: {name}")
        
        from_currency = get_currency_input("Enter the currency code to convert from: ", available_currencies)
        to_currency = get_currency_input("Enter the currency code to convert to: ", available_currencies)
        amount = float(input("Enter the amount to convert: "))
        
        converted_amount = convert_currency(from_currency, to_currency, amount)
        print(f"{amount} {from_currency} is {converted_amount} {to_currency}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
