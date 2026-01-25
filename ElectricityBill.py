units = int(input("Enter the number of units: "))

# Check invalid input
if units < 0:
    print("Invalid input!")
else:
    # Calculate bill
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 8
    else:  # units > 200
        bill = 100 * 5 + 100 * 8 + (units - 200) * 10

    # Add 10% surcharge if bill > 2000
    if bill > 2000:
        bill = bill + bill * 0.10

    # Show results
    print("Total units consumed:", units)
    print("Total bill: Rs.", bill)
