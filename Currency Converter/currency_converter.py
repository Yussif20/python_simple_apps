import requests 

init_currency = input("Enter an initial currency: ")
target_currency = input("Enter a target currency: ")

while True:
    try:
        amount = float(input("Enter the amount: "))
    except:
        print("The amount must be a numeric value!")
        continue
    if amount == 0:
        print("The amount must be greater than zero!")
        continue
    else:
        break

url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"

payload = {}
headers= {
  "apikey": "kuSughwAaAOYxCzZbvJozxmJXnOGsV8r"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
if status_code !=200:
    print("Sorry there was a error,please try again later")
    quit()

result = response.json()
print(result["result"])