principal = 15000 # Loan amount
rate = 5          # Annual interest rate in %
time = 2          # Time in years

# Calculation
simple_interest = (principal * rate * time) / 100

print(f"Simple Interest: ${simple_interest}")


principal = 5000  # Loan amount
rate = 5          # Annual interest rate in %
time = 2          # Time in years

# Calculation
compound_interest = principal * ((1 + (rate / 100)) ** time) - principal


print(f"Compound Interest: ${compound_interest}")
