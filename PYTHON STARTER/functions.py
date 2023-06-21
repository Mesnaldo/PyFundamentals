#FUNCTIONS
#Creating functions to understand how they work


#FUNCTION 1

#def add(x,y):
#    z = x+y
#    return z

#a = int(input())
#b = int(input())

#c = add(a,b)
#print(c)

#FUNCTION 2

#myList = [2,4,6,8,10]
#num = len(myList)

#def addList(List,numnum):
#    total = 0
#    for i in range(0,numnum,1):
#        total = total + List[i]
#    return total
    
#c = addList(myList,num)
#print(c)

#FUNCTION 3

'''
This part works, uncomment it to make it work
def add(x,y):
    a = x+y
    b = x-y
    c = x*y
    d = x/y
    return a,b,c,d

first_no = int(input("Enter the first no: "))
second_no = int(input("Enter the second no: "))

a,b,c,d = add(first_no,second_no) 
# 5 variables better than 1, to catch all the returns from the function
# If only c = function(x,y(passing arguments)) is done it returns but as list, [2,4,5,6] -> Like this
print("The sum is: ", a)
print("The dif is: ", b)
print("The mul is: ", c)
print("The div is: ", d)

'''

#FUNCTION 4

numbers = int(input("How many numbers do you want? "))

def Fnumbers(x):
    lstNum = []
    for i in range(x):
        no = int(input("Enter the numbers: "))
        lstNum.append(no)
    return lstNum

c = Fnumbers(numbers)
print(c)




