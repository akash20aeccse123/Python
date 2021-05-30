'''9. Program to print whether a given character is as 
uppercase or a lower case or a digit or any other 
character.'''

ch=input('Enter Character:')

if ch>='A' and ch<='Z':
    print("upper case character")
elif ch>='a' and ch<='z':
    print("lower case character")
elif ch>="0" and ch<="9":
    print("it is a digit")
elif ch==" ":
    print("You hitted space button")
else:
    print("You entered a special character")
