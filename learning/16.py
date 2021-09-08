meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())
tip=float(tip_percent/100)*meal_cost
tax=float(tax_percent/100)*meal_cost
print(round(meal_cost+tip+tax))