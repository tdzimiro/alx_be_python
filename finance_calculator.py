monthly_income = float(input("Enter your monthly income: "))
monthly_expense = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expense
print(f"Your monthly savings are: {monthly_savings}")
simple_annual_interest_rate = 0.05
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * simple_annual_interest_rate)
print(f"Your projected savings after one year, with interest is: {projected_savings}")
