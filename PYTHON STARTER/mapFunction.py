#Map Function use case
# 2 main inputs it take, 1) Function 2)Collection Eg.List

numbers = [1,2,3,4,5]

def multiply(x):
    mul = x*2
    return mul

#No need to use the paramenthis (), We normally use for to call functions
#So you got a function, you want to apply that to a collection?
#Be it dict, set, tuple
#Enters "MAP" FUNCTION

total = list(map(multiply, numbers))
print(total)
        
