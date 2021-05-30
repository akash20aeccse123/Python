'''4.program to calculate BMI(Body Mass Index) of a person.
 Body mass index is a simple calculation using a person's 
height and weight.
 formula is BMI=kg/m*m where kg is a person weight in 
kilograms and (m*m) is
 their height in meteres squared.'''

w=float(input("Enter weight  value in kg:"))
h=float(input("Enter height in meteres:"))
 
bmi=(w/(h*h))
print("Body mass index =",bmi)

