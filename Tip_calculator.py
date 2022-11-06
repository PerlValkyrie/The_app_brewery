# Tip calculator

print("Welcome to the tip calculator.")
total_bill = input("What was the total bill?\n")
total_bill = float(total_bill)
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15?\n")
tip_percentage = float(tip_percentage)

final_percentage = total_bill * (tip_percentage / 100)
bill_with_tip = final_percentage + total_bill

total_split = input("How many people to split the bill?\n")
total_split = float(total_split)
payout_per_person = bill_with_tip / total_split

# payout_per_person = round(payout_per_person, 2)
payout_per_person = "{:.2f}".format(payout_per_person)
print(f"Each person should pay: {payout_per_person}.")