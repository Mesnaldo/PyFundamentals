#TASK IS TO CREATE A CLASS WITH THE IDEA OF ADDING 2 COMPLEX NUMBERS
#Do this after learning classes, objects and about self. Then this would be a good task to test on.
#What is complex no?
#Well, add the imag part of one no with imag part of another
#Next, add real part of one no with another no
#Print it out

class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, self2):
        real = self.real + self2.real
        imag = self.imag + self2.imag
        result = Complex(real,imag)
        return result

number1 = Complex(50,-3)
number2 = Complex(30,-7)

complex_no = number1.add(number2)
print(complex_no)
print(complex_no.real)
print(complex_no.imag)


