# Input Validation with while Loops
while True:
  marks=float(input("Enter marks of subject:"))
  if(marks<0 or marks>100):
    break
  print(marks)


#   Conceptual Questions
# 1. Why is validation better handled with while loops than for loops?
#Ans:
# Validation is better handled with while loops because they repeat based on a condition and continue until valid input is provided, whereas for loops run a predetermined number of times.