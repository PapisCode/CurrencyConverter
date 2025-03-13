# Hardcoded currencies with currency name and exchange rate

currencies = {
        1: ('Indian Rupee', 87.072167),
        2: ('Euro', 0.92467496),
        3: ('Yen', 147.41483),
        4: ('Ringgit', 4.4271591),
        5: ('British Pound', 0.7757534),
        6: ('Canadian Dollar', 1.4358244)
    }

# Printing each currency's key and name

for key, value in currencies.items():
    print(f"{key}. {value[0]}")

# Taking input from user as integer and saving in variable amount

amount = int (input("Please enter your choice of currency (1-6)"))

# If statement to ensure choice is valid

if amount in currencies:

    # saving the selected name, and exchange rate in variables

    selected_name, selected_currency = currencies[amount]
    
    # printing the number and name of the currency selected

    print(f"You have chosen currency #{amount}: {selected_name}")

    # calculating to USD the conversion and saving in a variable

    converted_amount = 100 * selected_currency

    # printing and showing to 2 decimal places

    print(f"Here is 100 USD in {selected_name}: {converted_amount:.2f}  ")

# else statement for incorrect input
 
else:
    print("Sorry, your input is invalid.")

# displaying thank you message before exiting
print("Thank you for using the Currency Converter program.  Bye!")
