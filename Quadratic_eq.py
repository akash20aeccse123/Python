import cmath

a=float(input("Enter 1st Number:"))
b=float(input("Enter 2nd Number:"))
c=float(input("Enter 3rd Number:"))

d=b**2-4*a*c
soln1=(-b+cmath.sqrt(d))/2*a
soln2=(-b-cmath.sqrt(d))/2*a
print("Solutions are {} and {}".format(soln1,soln2))

