
def result_cal(marks):
  total=sum(marks)
  count=len(marks)
  return total/count

def grade(average_marks):
  if(average_marks>90):
    grade='A+' 
  elif average_marks>80:
    grade='A'
  elif average_marks>70:
    grade='B+'
  elif average_marks>60:
    grade='B'
  elif average_marks>50:
    grade='C+'  
  elif average_marks>40:
    grade='C'
  else:
    grade='F'

  return grade
 
def output(average,grade):
  print(f"grade :",grade)
  print(f"average :",average)

average_marks=result_cal([50,80,100])
grade=grade(average_marks)
output(average_marks,grade)

# Conceptual / Brainstorming Questions 
# 1. Why is returning values better than printing inside functions? 
# Reusability : returned valued can be reused for further calculation ,testing , or can reuse that return value by  passing to other functions.





