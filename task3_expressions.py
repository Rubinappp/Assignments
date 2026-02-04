# student performance score:

assignment_score=float(input("enter assignment score:"))
lab_score=float(input("enter lab score:"))
exam_score=float(input("enter exam score:"))
final_score=assignment_score+lab_score+exam_score

print(f"Final score of the result: {final_score}")

# Reasoning Questions
# 1. Why is operator precedence critical in scientific or financial software?
# Operator precedence determines the order of operations. so calculation will be wrong with wrong precedence.
# Eg:
# Rocket trajectory calculations off :mission failure, satellite lost
# Loan calculations wrong : bank loses millions or customers overcharged

# 2. How could floating-point precision errors affect real-world applications?
# Computers can't represent all decimal numbers exactly in binary. 
# Small rounding errors accumulate and cause significant problems in critical systems.
# Eg:
# Price discrepancies:  shows $10.00 but charge is $10.01
# Inventory mismatches: Calculated stock value ≠ actual result in financial reporting errors
