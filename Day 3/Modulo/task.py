# introduction
print("Welcome to the Number Check Program!")

# check number
number = int(input(
    "Type in a number to check if it's odd or even.\n"
    "Your number: "
))

# print result
if number % 2 == 0:
    print(f"{number} is even")
else :
    print(f"{number} is odd")