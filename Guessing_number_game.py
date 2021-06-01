'''6. Program to implement ‘guess the number’ game. 
Python generates a number randomly in the range 
[10,50]. The user is given five chances to guess a 
number in the range 10<=number<=50.'''

import random
number= random.randint(10,50)
c=0
while c<5:
    guess=int(input('Enter Number in range 10....50:'))

    if guess==number:
        print("You Win!!")
        break
    else:
        c=c+1
if not c>5: #Wheter the loop terminates after 5 iteration 
    print("You loss:""The number is=",number)


