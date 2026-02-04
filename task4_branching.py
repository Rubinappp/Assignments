# academic decision system:

attendance=float(input("Percentage of attendance:"))
total_marks=float(input("Enter total marks:"))

if(attendance<70):
  print("Not eligibe")
else:
  if(total_marks>=90):
    grade='A+'
    
  elif(total_marks>80):
    grade='A'

  elif(total_marks>=70):
    grade='B+'
    
  elif(total_marks>60):
    grade='B'
  elif(total_marks>50):
    grade='C+'
  elif(total_marks>40):
    grade='C'
  else:
    grade=None

  print(grade)
