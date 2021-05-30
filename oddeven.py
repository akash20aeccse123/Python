'''1. Program that takes a number and checks whether 
the given number is odd or even.'''

n=int(input("Enter number to check:"))
if n<0:
    print("Negative value does not exists.")
elif n%2==0:
    print("Number is Even")
else:
    print("Number is Odd")
 
