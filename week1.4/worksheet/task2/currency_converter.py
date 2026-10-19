
"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name: Marcus Florin
"""

def currency_converter(amount, from_currency, to_currency):

    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }

    amount = float(amount) #standerdise data type of amount

    conversion_rate_country = conversion_rate.get(from_currency) 
    conversion_rate_value = float(conversion_rate_country.get(to_currency))

    if amount >= 0:

        conversion = amount * conversion_rate_value
        conversion = round(conversion,2)

        return conversion

    else:
        
        return 0.0

print(currency_converter(101,'GBP','CNY'))
