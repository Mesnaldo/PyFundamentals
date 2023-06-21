#Create a student class
#Create student1,2,3 objects
#Things you would need is firstname,lastname
#method that inputs grade
#method that prints the students grade
#method that averages the student grade
#method that prints student high grade
#method that prints student low grade

class Student:
    def __init__(self,f,l,i):
        self.firstname = f
        self.lastname = l
        self.input = i

    def input_grades(self):
        for number in range(self.input):
            grade = int(input("Enter the grades: "))
            grades.append(grade)

    # -----> THIS IS ANOTHER WAY WE COULD HAVE DONE
    #def input_grades(self,i):
    #    print("The number of grades you want is: ", i)
    #    self.input = i
    #    grades = []
    #    for number in range(i):
    #        grade = int(input('Enter the grades: '))
    #        grades.append(grade)

    def print_grades(self):
        print("\nYour Grades are: ")
        for grade in grades:
            print(grade)

    def average(self):
        total = 0
        for grade in grades:
            total = total + grade
        average = total/self.input
        print("Your Average Grade is: ", average)
    
    def highGrade(self):
        max = 0
        for grade in grades:
            if max<grade:
                max = grade
        print("Your high grade is",max)

    def lowGrade(self):
        min = 100
        for grade in grades:
            if min>grade:
                min = grade
        print("Your lowest grade is: ",min)
            
#----> For that another way ---> student1.input_grades(3)
grades = []
student1 = Student("Shyam","Shanckin",3)
print(student1.firstname, student1.lastname)

student1.input_grades()
student1.print_grades()
student1.average()
student1.highGrade()
student1.lowGrade()


    