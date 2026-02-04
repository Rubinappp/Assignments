# scholarship eligibility checker:
cgpa=float(input("Enter cgpa:"))
income=float(input("Monthly income:"))
attendance=float(input("Attenadance (%)"))
if(cgpa>=3.5 and income<=20000 and attendance>70):
  print("You are eligible for scholarship program")
else:
    print("You are not eligible for scholarship program")