'''9.write a program to input two numbers and swap them.
 do not use 3rd variable
 do not use arithmatics
 do not use bitwise operator'''

a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))

print("Before swap a=",a)
print("Before swap b=",b)


a=a^b
b=a^b
a=a^b
print("After swap a=",a)
print("After swap b=",b)
