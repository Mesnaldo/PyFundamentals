class Rectangle:
     def __init__(self,c,l,w):
          self.color = c
          self.length = l
          self.width = w
          #self.area = self.l * self.w #I CAN DO HERE AS WELL!
     def area(self):
          self.area = self.length*self.width
          return self.area
     def per(self):
          self.perimeter = 2*self.length + 2*self.width
          return self.perimeter
     def diagonal(self):
          self.diagonal = ((((self.width)**2)+((self.length)**2))**(1/2))
          return self.diagonal
     def volume(self,h): 
          # ----> As you have seen, I'm introducing new variable
          # ----> You can do this without addig it to class
          # Flexiblity is there
          self.height = h
          self.volume = self.length*self.width*self.height
          return self.volume


myrect1 = Rectangle('red',2,3)

print("myrect1 color is: ", myrect1.color)
print('myrect1 length is: ', myrect1.length)
print("myrect1 width is: ",myrect1.width)
print("myrect1 area is: ",myrect1.area())
print("myrect1 perimeter is: ", myrect1.per())
print("myrect1 volume is: ", myrect1.volume(10))
print("myrect1 diagonal is: ",myrect1.diagonal())


#Create a student class
#Create student1,2,3 objects
#Things you would need is firstname,lastname
#method that inputs grade
#method that prints the students grade
#method that averages the student grade
#method that prints student high grade
#method that prints student low grade

