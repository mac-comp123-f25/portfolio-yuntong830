money = 732
dollars = money // 100
money = money % 100
quarters = money // 25
money = money % 25
dimes = money // 10
money = money % 10
nickles = money // 5
money = money % 5
pennies = money
print(dollars, quarters, dimes, nickles, pennies)