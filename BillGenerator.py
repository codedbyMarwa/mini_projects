name=input("Item name: ")
price=float(input("Item price: "))
quantity=int(input("Item quantity: "))

total=price*quantity

print(f"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Item: {name}
Price: {price}
Quantity: {quantity}
TotalBill: {total}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")