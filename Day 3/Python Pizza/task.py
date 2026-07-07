# introduction
print("Welcome to Python Pizza Deliveries!")

# choose pizza
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# init bill
bill = 0

# size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

# pepperoni
if pepperoni == "Y" and size == "S":
    bill += 2
elif pepperoni == "Y" and size != "S":
    bill += 3

# extra cheese
if extra_cheese == "Y":
    bill += 1

# print bill
print(f"Your final bill is: ${bill}.")