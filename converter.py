import requests

# 1. The public API URL providing live conversion data relative to INR
url = "https://open.er-api.com/v6/latest/INR"

# 2. Fire an HTTP GET request to the URL
response = requests.get(url)

# 3. Convert the raw web response directly into a Python Dictionary
data = response.json()

# 4. Print the raw data to see what the server sent us
print("\n--- RAW API RESPONSE ---")
print(data)

# 5. Extract the rates dictionary
#rates = data["conversion_rates"]

# 6. Get the amount from the user
inr_amount = float(input("Enter amount in INR: "))

#7 which currency do you want
target_currency = input("Enter target currency code (USD, EUR, GBP): ").upper()

# Check if the currency code exists in our rates dictionary
if target_currency in data:
    # Look up the rate and multiply it by the user's amount
    converted_amount = inr_amount * data[target_currency]
    print(f"\n{inr_amount} INR is equal to {round(converted_amount, 2)} {target_currency}")
else:
    print("\nSorry, that currency code is not supported.")
