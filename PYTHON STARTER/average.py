#TASK IS :

# HOW MANY GRADES YOU HAVE? INPUT
# PUT THAT IN THE ARRAY
# AVERAGE THE GRADES NEXT
# PRINT THE AVERAGE AND ALL THE GRADES
# 3 FOR LOOP
# TO INPUT THE ARRAY
# AVERAGE THE ARRAY
# PRINT THE GRADES OUT

num_grades = int(input("\nHow many Grades do you have? "))
grades=[]
for i in range(num_grades):
    grade = int(input("Enter the grades now: "))
    grades.append(grade)
average=0
for i in grades:
    average = average+i
    sum = average/num_grades
print("\nYour average grades are:", sum)
print('\nHere are your Grades: ')
for i in grades:
    print(i)
    