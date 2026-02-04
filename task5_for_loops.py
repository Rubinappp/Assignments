# marks analyzer:
n=int(input("Enter the number of subject: "))
total=0 # accumulator 
highest=0
lowest=100
for i in range(1,n+1):
  marks=float(input(f"Enter marks for subject{i}:"))
  total+=marks
  if(marks>highest):
    highest=marks
  if(marks<lowest):  
    lowest=marks
    
average=total/n
print("Total obtained marks:", total)
print("Average marks:", average)
print("Highest mark:", highest)
print("Lowest mark:", lowest)









# n=int(input("Enter the number of subject"))
# marks=[]
# for i in range(1,n+1):
#   marks.append(int(input(f"Enter marks for subject{i}:")))
# total=sum(marks)
# average=total/n
# highest=max(marks)
# lowest=min(marks)
# print("Total obtained marks:", total)
# print("Average marks:", average)
# print("Highest mark:", highest)
# print("Lowest mark:", lowest)