num1input = int(input("Nummer 1: "))
teken1input = input("Teken 1: ")
num2input = int(input("Nummer 2: "))
if teken1input == "-":
    result = num1input - num2input
elif teken1input == "+":
    result = num1input + num2input
elif teken1input == "*":
    result = num1input * num2input
elif teken1input == "/":
    result = num1input / num2input
print("Result: ", result)