def vat_calculator(price):
    
    result = price + (price*7/100)
    return result
mo = int(input())
print(vat_calculator(mo))   