# basic financial calculator:

# monthly_income=input("Enter your monthly salary:") # invalid literal
monthly_income=float(input("Enter your monthly salary:"))
monthly_expenses=float(input("Enter your monthly aexpenses:"))
print(monthly_income )
print(monthly_expenses )

# Reasoning Questions
# 1. Why does Python delay type errors until runtime, unlike compiled languages?
# Ans:
# Python is an interpreted language with dynamic typing so  it doesn't have a compilation step that checks types beforehand.

# 2. How could unvalidated user input compromise real-world systems (e.g., billing,voting)?
#Ans:
# - If systems don't check/validate input,user may input invalid strings or values so System may crash at run time.Even attackers can inject malicious data that causes incorrect behavior, data corruption, or security breaches.
# - 
# Eg:
# Billing: Negative quantity → refunds instead of charges
# Voting: Multiple votes or negative votes → election fraud