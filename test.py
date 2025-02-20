#total_hour = 40
#money_per_hour = 10

def wages(total_hour, money_per_hour):
    print(f"I made ${total_hour * money_per_hour} weekly as a delivery guy")
money_per_hour = int(input("how much do you make an hour?\n"))
wages(40, money_per_hour)