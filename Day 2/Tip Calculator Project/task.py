print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percentage = tip / 100
tip_total = tip_percentage * bill
bill_total = bill + tip_total
bill_split = bill_total / people
total = round(bill_split, 2)

print(f"Each person should pay: ${total}")
