def currency_converter():
    # Fixed exchange rates (as of example)
    rates = {
        'USD': 1.0,
        'INR': 83.10,
        'EUR': 0.93,
        'JPY': 157.20,
        'GBP': 0.79
    }

    print("Available currencies: ", ', '.join(rates.keys()))
    
    from_currency = input("Convert from (e.g., USD): ").upper()
    to_currency = input("Convert to (e.g., INR): ").upper()
    amount = float(input("Amount: "))

    if from_currency in rates and to_currency in rates:
        usd_amount = amount / rates[from_currency]
        converted = usd_amount * rates[to_currency]
        print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")
    else:
        print("Invalid currency code.")

currency_converter()
