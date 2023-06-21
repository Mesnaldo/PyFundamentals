# In while loop I give the counters explicitly
#Basic intro of how while works
#Just prompt grades from user, and use one while for taking input
#Another for printing it out



num_grades = int(input("How many grades you want? "))

i = 0  #counter
lst_grades = []
while(i<num_grades):
    grades = int(input("Enter the grades: "))
    lst_grades.append(grades)
    i = i + 1 #must needed for the while to top after reaching the threshold


print("\nThe Grades are: ")

j=0
while(j<num_grades):
    print(lst_grades[j])
    j=j+1

print("Thats All Folks!")



