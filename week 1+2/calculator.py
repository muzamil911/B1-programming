# calculator.py
# This program calculates profit and profit margin based on user input for revenue and costs.
#lets go:

# Get user input
revenue = float(input("Enter total revenue: "))
costs = float(input("Enter total costs: "))

# Calculate profit and profit margin
profit = revenue - costs
profit_margin = (profit / revenue) * 100 if revenue != 0 else 0

# Display formatted results
print("\n----- Results -----")
print(f"Revenue: ${revenue:,.2f}")
print(f"Costs:   ${costs:,.2f}")
print(f"Profit:  ${profit:,.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")