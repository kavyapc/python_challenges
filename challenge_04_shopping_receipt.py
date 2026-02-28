
name1 = (input("enter item1 name:"))

price1 = float(input("enter item1 price:"))

name2 = (input("enter item2 name:"))

price2 = float(input("enter item2 price:"))

name3 = (input("enter item3 name:"))

price3 = float(input("enter item3 price:"))
print("------------------------------------------")
print(f"{name1}      ${price1}")
print(f"{name2}      ${price2}")
print(f"{name3}      ${price3}")
print("------------------------------------------")
total = price1+price2+price3

print(f" TOTAL =    ${total:.2f}")