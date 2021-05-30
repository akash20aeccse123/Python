'''10.write a program to input three numbers and swap them 
as this:
 1st number becomes the 2nd number,
 2nd number becomes the 3rd number,
 3rd number becomes the 1st number.'''

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))

print("Before swap a=",a)
print("Before swap b=",b)
print("Before swap c=",c)


a,b,c=b,c,a

print("After swap a=",a)
print("After swap b=",b)
print("After swap c=",c)

