
initial_savings = 300  # base amount
monthly_deposit = 50  # depositing each month
months = 12             # taotal time

# Calculation
total_savings = initial_savings
for _ in range(months):
    total_savings += monthly_deposit


print(f"Total savings  got after {months} months: ${total_savings}")

