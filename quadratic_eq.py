'''10. Program to calculate and print the roots of a 
quadratic equation.'''
import cmath
a=int(input("Enter 1st Number:"))
b=int(input("Enter 2nd Number:"))
c=int(input("Enter 3rd Number:"))

d=b*b-4*a*c
soln1=-b+cmath.sqrt(d)/2*a
soln2=-b-cmath.sqrt(d)/2*b
print("The solutions are {} and {}".format(soln1,soln2))

