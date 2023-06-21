#UNDERSTANDING FOR LOOP
#USING FOR LOOP DO THE FOLLOWING TASKS
# 1.Take grades from users and store them in a list
# 2.Find the average grades
# 3.Find the lowest grades
# 4.Find the highest grades


num_grades = int(input("Enter the no of the grades: "))

grades=[]
for i in range(num_grades):
    grade = int(input("Enter the grade: "))
    grades.append(grade)

average = 0
for j in grades:
    average = average + j
sum = average/num_grades
print('\nYour average of grades are: ',sum)

max=0
for k in grades:
    if max<k:
        max = k
print("\nThe lowest grade you have got is: ",max)

min=1000
for l in grades:
    if min>l:
        min = l
print("\nThe highest grade you have got is: ",min)


        






