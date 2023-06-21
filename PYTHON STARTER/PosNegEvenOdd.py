# CONDITIONALS
#Using if conditons do this :
#POSITIVE EVEN
#POSITIVE ODD 
#NEGATIVE ODD
#EGATIVE EVEN
#ZERO

num = int(input("Enter a number: "))

rem = num%2

if rem == 0 and num > 0:
    print("POSITIVE EVEN")

if rem == 0 and num < 0:
    print("NEGATIVE EVEN")

if rem!=0 and num > 0:
    print("POSITIVE ODD")

if rem!=0 and num < 0:
    print("NEGATIVE ODD")

if num == 0:
    print("ZERO")