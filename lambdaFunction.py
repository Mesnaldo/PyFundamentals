# SYNTAX : lambda arguement : Expression
# Small fuction instead of using def and stuff

# Small program that just prints out whatever no we give in as input
#It doubles by multiplying by 2

#Think of double like the function name that you are gonna do

#Lambda Function 1
double = lambda x : 2*x 

#Well you call the function,input the arguement, store in variable, print it out
result = double(100)
print(result)

#Another lambda for squaring the no as in x**2
# function_name = lamda input : what you gonna do with the input(A.K.A return statement)

#Lambda Function 2
square = lambda x : print("The square of the no is", x**2)
#Call the function now
square(10)

#Lambda Function 3
#Let's do addition and multiplication
addition = lambda x,y : print("The addition is: ", x+y)
multiplication = lambda x,y : print("The multiplication is: ", x*y)

addition(9000,5000)
multiplication(7,7)



