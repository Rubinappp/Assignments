#Menu-driven student utility system
name=[]
age=[]
subject1_marks=[]
subject2_marks=[]
subject3_marks=[]



def student_details():
  global name,age
  n=int(input("Enter the number of students:"))
  for i in range(1,n+1):
    name.append(input("Name of the student:"))
    age.append(int(input("Enter age of the student")))
 
def student_marks():
  global subject1_marks,subject2_marks,subject3_marks
  for i in range(1 ,len(name)+1):
    subject1_marks.append(float(input(f"Enter marks of student{i} in subject1:")))
    subject2_marks.append(float(input(f"Enter marks of student{i} in subject2:")))
    subject3_marks.append(float(input(f"Enter marks of student{i} in subject3:")))

   
def result_summary():
    global subject1_marks,subject2_marks,subject3_marks,age,name
    for i in range(len(name)):
       total = subject1_marks[i] + subject2_marks[i] + subject3_marks[i]
       average = total / 3

       print(f"  Name       : {name[i]}")
       print(f"  Age        : {age[i]}")
       print(f"  Subject 1  : {subject1_marks[i]:.2f}")
       print(f"  Subject 2  : {subject2_marks[i]:.2f}")
       print(f"  Subject 3  : {subject3_marks[i]:.2f}")
       print(f"  Total      : {total:.2f}")
       print(f"  Average    : {average:.2f}")
     
  
    print("highest in subject1:" ,max(subject1_marks))
    print("highest in subject2:" , max(subject2_marks))
    print("highest in subject3:" , max(subject3_marks))
    print("lowest in subject1:" ,min(subject1_marks))
    print("lowest in subject2:" , min(subject2_marks))
    print("lowest in subject3:" , min(subject3_marks))
  
while True:
  print("1. Enter student details .")
  print("2. Enter marks ")
  print("3. View result summary ")
  print("4. Exit ")

  choice=int(input("Enter number between 1 to 4: "))
  if(choice==1) :
    student_details()
  elif(choice==2):
    student_marks()
  elif(choice==3):
     result_summary()
  elif(choice==4):
    break
  



#   Reasoning Questions 
# 1. What changes would be required to convert this into a web application?
#Ans:
# To convert this program into a web application, console input/output must be replaced with HTML forms and pages, the menu loop replaced with web routes using a framework like Flask or Django, lists replaced by a database, and HTTP request handling, validation, and security added.


  


