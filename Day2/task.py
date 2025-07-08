
total_bill = float(input("What was the total bill?\n"))

tip_percent = float(input("What percentage tip would you like to leave? 10, 12, or 15?\n"))

split = float(input("How many people to split the bill?\n"))

total_after_tip = total_bill + (total_bill * (tip_percent/100))

total_after_split = total_after_tip/split

print(f"Each person should pay: ${round(total_after_split,2)}")