#1.Take a number from the user, check if it's even or odd, and print the result.
num = int(input("enter a number:"))
if num % 20 == 0:
    print("number is even")
else:
    print("number is odd")

#2.Take the user's age, check if it's 18 or above. If yes, print "You can vote", otherwise print "You cannot vote".
age = int(input("enter your age:"))
if age >= 18:
    print("yor can vote")
else:
    print("you can not")


#3.Take the user's marks (0-100), and decide their grade:

#90+ → "A"
#70-89 → "B"
#50-69 → "C"
#Below 50 → "Fail"
marks = int(input("enter your marks:"))
if marks>= 90:
    print("grade A")
elif marks >= 70:
    print("grade B")
elif marks >= 50:
    print("grade C")
else:
    print("fail")

#4.Take two numbers from the user, and print which one is bigger (or if they're equal, mention that too).
num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
if num1 > num2:
    print(num1  , "greater")
elif num2 > num1:
    print(num2 , "greater" )
else:
    print("both numbers are equal")  

#5.take the users age and a yes/no input.if age is 18+ and they have an id.print entry allowd,otherwise print entery denied.
age = int(input("enter your age:"))
if age >= 18:
    print("entry allowed")
else:
    print("entry denied3")