'''8. Program to reads three numbers the print them in 
ascending order.'''

x=int(input("Enter Number 1:"))
y=int(input("Enter Number 2:"))
z=int(input("Enter Number 3:"))
min1=mid=max1=None

if x<y and x<z:
    if y<z:
        min1=mid=max1=x,y,z
    else:
        min1=mid=max1=x,y,z

elif y<x and y<z:
    if x<z:
        min1=mid=max1=y,x,z
    else:
        min1=mid=max1=y,x,z
else:
    if x<y:
        min1=mid=max1=z,x,y
    else:
        min1=mid=max1=z,x,y
print("Numbers in ascendind order=",min1,mid,max1)

