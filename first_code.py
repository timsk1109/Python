print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0

if size == "S":
  bill += 10
elif size == "M":
  bill += 15
else:
  bill +=20

if add_pepperoni == "Y":
  bill += 3
if extra_cheese == "Y":
  bill += 2

print(f"your bill is ${bill}.")