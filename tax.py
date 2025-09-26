def add_tax(price, tax_rate):
    tax_amt = price * tax_rate
    return price + tax_amt
print(add_tax(25.99,0.0725))
'''
Local environment
   price   25.99
   tax_rate  0.0725
   tax_amt   1.884275
   return 27.874274999999997
'''
add_tax(25.99, 0.0725)




