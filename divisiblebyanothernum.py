'''4. Program to test the divisibility of a number with 
another number.'''

n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))

remainder=n1%n2
if remainder==0:
    print(n1,'is divisible by ',n2)
else:
    print(n1,'is not  divisible by',n2)
