'''2. Program to accept three integers and print the 
largest of the three.'''

a=int(input("Enter 1st Number:"))
b=int(input("Enter 2nd Number:"))
c=int(input("Enter 3rd Number:"))

if a>b and a>c:
    print(a,"is largest number")
elif b>a and b>c:
    print(b,'is largest number')
else:
    print(c,'is largest number')
