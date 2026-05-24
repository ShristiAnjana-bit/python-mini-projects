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

#5. Extract the specific currency rates from the big data dictionary
rates = data["conversion_rates"]

#6.Now,get the user's input for the INR amount
inr_amount =float(input("Enter amount in INR: "))