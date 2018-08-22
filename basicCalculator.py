# add two integers
def add(x, y):
    return x + y

# subtract two integers
def subtract(x, y):
    return x - y

# multiply two integers
def multiply(x, y):
    return x * y

# divide two integers
def divide(x, y):
    return x / y

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1, 2, 3, 4): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
    print(add(num1, num2))

elif choice == 2:
    print(subtract(num1, num2))

elif choice == 3:
    print(multiply(num1, num2))

elif choice == 4:
    print(divide(num1, num2))

else:
    print("invalid input")

