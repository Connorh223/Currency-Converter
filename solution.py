import requests

from_currency = str(
    input("Enter in the currency you would like to convert from: ")).upper()

to_currency = str(
    input("Enter in the currency you would like to convert to: ")).upper()


amount = float(input("Enter in the amount of money: "))

response = requests.get(
    f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

#print(response.status_code)

print (f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")