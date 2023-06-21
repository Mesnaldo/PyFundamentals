#SIMPLE SORTING PROGRAM IN PYTHON

#Sort the grades in order

#Getting the toal no of grades
num_grades = int(input("\nHow many Grades do you have? "))
grades=[]
#Getting the grades and saving it to a list using append
for i in range(num_grades):
    grade = int(input("Enter the grades now: "))
    grades.append(grade)
print(grades)
#Algo for sorting the list
#First for loop to go through it couple of times
for j in range(0,num_grades-1, 1):
#Second for loop is for going through it and swapping them, like next-next with comparison
    for k in range(0,num_grades-1, 1):
        if grades[k] < grades[k+1]:
            temp = grades[k]
            grades[k] = grades[k+1]
            grades[k+1] = temp
print("Your sorted list is: ",)

#Printing all the grades
for l in grades:
    print(l)





