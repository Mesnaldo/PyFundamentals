#MY OWN EXAMPLE TO UNDERSTAND CLASS, OBJECT, METHOD, DATA ATTRIBUTE, VALUE

class Laptop:
    # If you have set the initial value in "init", then every object will by default get those inital values only.
    # If you want every object( I think of this as some entity)
    #Object is like entity, Phone, Speaker, Student, Teacher, Anything.
    #Class is container of many entity, right?
    #Here Laptop is class
    #And there are many laptops right in the world
    #So Objects can represent many entity here laptop
    #And some method can be used to call on this laptop object to check something
    #Here i am checking the budget
    # Every obj when created first goes to special constructor -> "INIT"
    # So if you give some default value, then that value only the object will take
    # Not anything else, even if you give manually like obj.data attribute = value
    # That would be ignored
    #So better leave it just by giving its own name eg.self.brand = brand So no default value
    #So you can give your own default value here

    def __init__(self,brand,price,color):
        self.brand = brand
        self.price = price
        self.color = color

    def budget(self):
        #Using self i can go through any data attribute of an object
        #Self is a must, and the first attribute
        if self.price<=80000:
            return True
        else:
            return False
        
laptop1 = Laptop('Dell',75000,'white')
l1_is_budget_okay =laptop1.budget()
print(l1_is_budget_okay)

laptop2 = Laptop('MAC',100000,'grey')
l2_is_budget_okay = laptop2.budget()
print(l2_is_budget_okay)

print(laptop2.brand) 
print(laptop2.price)
print(laptop2.color)

# I can access the object's data attribute as well
# ------>   "objectname.data attribute"






    

