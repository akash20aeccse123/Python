yr=int(input("Enter year :"))
if(yr%4==0 and yr%100!=0 or yr%400==0):
    print(yr,"is Leap year.")
else:
    print(yr,"is Not a leap year.")
