monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
yearly_savings = monthly_savings * 12
projected_savings = yearly_savings + (yearly_savings * 0.05)
print("Projected savings after one year, with interest, is:", int(projected_savings))
