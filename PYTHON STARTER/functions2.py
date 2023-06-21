'''
def inputGrades
def printGrades
def AvgGrades
def highLow

print inputGrades
print printGrades
print AvgGrades
print highLow

Do this but using functions only

'''

num_grade = int(input("How many grades you want? "))

grades = []
def inputt(x):
    for i in range(x):
        grade = int(input("Enter the grades: "))
        grades.append(grade)

def printt(y):
    for i in range(0,y,1):
        print(grades[i])

inputt(num_grade) #F1
printt(num_grade) #F2


def avg(z):
    total = 0
    for i in z:
        total = total + i
    sum = total/num_grade
    print('The average is', sum)

avg(grades)

def highLow(q):
    max = 0
    for i in q:
        if max<i:
            max = i
    print("The high grade you got is: ", max)

    min = 1000
    for i in q:
        if min>i:
            min = i
    print("The low grade you got is: ", min)

highLow(grades)

    











