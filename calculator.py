expression = input("Enter an expression: ")

parts=expression.split()

if len(parts)==3:
    numb1=float(parts[0])
    operator = parts[1]
    numb2 = float(parts[2])

if operator == '+':
    result = numb1 + numb2
elif operator=='-':
    result = numb1 -numb2
elif operator=='*':
    result = numb1 * numb2
elif operator == '/':
    result = numb1 / numb2
else:
    print("Enter an expression in the format: 'number operator number'")

print("Result:", result)