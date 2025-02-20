#total_hour = 40
#money_per_hour = 10

def wages(total_hour, money_per_hour):
    if money_per_hour > 0:
      print(f"I made ${total_hour * money_per_hour} weekly as a delivery guy")
    else:
       print("you entered an invaild input.")
money_per_hour = int(input("how much do you make an hour?\n"))
wages(40, money_per_hour)