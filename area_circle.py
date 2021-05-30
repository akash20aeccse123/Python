'''6. Program to display a menu for calculating area of a 
circle or perimeters of a circle.'''

r=float(input('Enter Radius:'))
print("1.Calculate Area")
print("2.Calculate Perimeter")
ch=int(input("Enter Your Choice(1 or 2)="))
if ch==1:
    area=3.14*r*r
    print("Area of Circle=",area)
else:
    perimeter=2*3.14*r
    print("Perimeter of the Circle=",perimeter)
