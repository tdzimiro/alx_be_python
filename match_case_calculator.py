numb1 = float(input("Enter the first number: "))
numb2 = float(input("Enter the second number: "))
operation  = input("Choose the operation(+, *, /, -): ")

match operation:
    case "+":
      output = numb1 + numb2
    case "*":
      output = numb1 * numb2
    case "/":
      if numb2 != 0:
        output = numb1 / numb2
      else:
        output = "Cannot divide by zero"
    case "-":
      output = numb1 - numb2
    case _:
     output = "Invalid entery"

print(f"The result is {output}")
