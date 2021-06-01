'''5. Program to calculate and print the sum of even 
and odd integers of the first n natural numbers.'''

n=int(input("Enter Number :"))
i=1
sum_even=0
sum_odd=0
while i<=10:
    if i%2==0:
        sum_even=sum_even+i
    else:
        sum_odd=sum_odd+i
    i=i+1
print("The Sum of Even integers=",sum_even)
print("The Sum of Odd integers =",sum_odd)


