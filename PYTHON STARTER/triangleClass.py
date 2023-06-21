#Another Class Example
#Create class triangle
#Create the data attributes necessary
#Then, create method, that does perimeter of the triangle

class Triangle:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        perimeterr = self.a + self.b + self.c
        return perimeterr
    
triangle1 = Triangle(10,20,30)

perimeter_of_triangle = triangle1.perimeter()

print(perimeter_of_triangle)