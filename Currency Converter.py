
import PyQt5
import requests


class currency_converter:
    def get_user_input():
        try:
            amount = input("Amount: ")
            if amount.isdigit():
                amount = int(amount)
            else:
                amount = float(amount)
                if amount <= 0:
                    raise ValueError("Amount must be greater than 0")
        except ValueError:
                print("Invalid amount. Please enter a valid number greater than 0.")
        curr1 = str(input("From: ").upper())
        curr2 = str(input("To: ").upper())
        return curr1, curr2, amount
    def bring_currencies(curr1, curr2, amount):
        api_url = "https://v6.exchangerate-api.com/v6/8df632a3d20e3d7a62433030/latest/pair/{curr1}/{curr2}/{amount}"
        response = requests.get(api_url)
        data = response
        if response.status_code == 200:#200 is an http code that means ok, request was successful, and others like 404 error mean not found
            data = response.json()
            print("{amount} {curr1} is equal to {converted_amount:.2f} {curr2}")
            try:
                conversion_rate = data['rates'][curr2]
                converted_amount = amount * conversion_rate
                print (converted_amount)
            except KeyError:
                print("Error: Invalid currency code or conversion rate not found.")
        else:
            print("Error:", response.status_code)
            return None
    
    
    
if __name__ == '__main__':
    curr1, curr2, amount = currency_converter.get_user_input()
    converted_amount = currency_converter.bring_currencies(amount, curr1, curr2)
    if converted_amount is not None:
        print("{amount} {curr1} is equal to {converted_amount:.2f} {curr2}")
        
        
import requests


class currency_converter:
    def get_user_input():
        try:
            amount = input("Amount: ")
            if amount.isdigit():
                amount = int(amount)
            else:
                amount = float(amount)
                if amount <= 0:
                    raise ValueError("Amount must be greater than 0")
        except ValueError:
                print("Invalid amount. Please enter a valid number greater than 0.")
        curr1 = str(input("From: ").upper())
        curr2 = str(input("To: ").upper())
        return curr1, curr2, amount
    def bring_currencies(curr1, curr2, amount):
        api_url = "https://v6.exchangerate-api.com/v6/this where i put my api key/latest/pair/{curr1}/{curr2}/{amount}"
        response = requests.get(api_url)
        data = response
        if response.status_code == 200:#200 is an http code that means ok, request was successful, and others like 404 error mean not found
            data = response.json()
            print("{amount} {curr1} is equal to {converted_amount:.2f} {curr2}")
            try:
                conversion_rate = data['rates'][curr2]
                converted_amount = amount * conversion_rate
                print (converted_amount)
            except KeyError:
                print("Error: Invalid currency code or conversion rate not found.")
        else:
            print("Error:", response.status_code)
            return None
    
    
    
if __name__ == '__main__':
    curr1, curr2, amount = currency_converter.get_user_input()
    converted_amount = currency_converter.bring_currencies(amount, curr1, curr2)
    if converted_amount is not None:
        print("{amount} {curr1} is equal to {converted_amount:.2f} {curr2}")

