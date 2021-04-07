yr=int(input('enter year to check:'))

if yr%4==0 and yr%100!=0 or yr%400==0:
    print(yr,'is Leap year')
else:
    print(yr,'is not a leap year')
