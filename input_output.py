#1.Take the user's name as input, then print: "Hello, <name>!"
name = input("enter your name:")
print("hello," + name+ "!")


#2.Take the user's age as input, convert it to int(), add 5 to it, and print: "In 5 years, you will be X years old."
age = input("enter your age:")
age = int(age)
future_age = age + 5
print("in 5 years, you will be:", future_age,"years_old")

#3.Take two numbers as input from the user, convert both to int(), and print their sum.
num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))

num1 = int(num1)
num2 = int(num2)

print(num1 + num2)

#4.Take the user's name and city as two separate inputs, then print one line: "<name> lives in <city>"
name = input("enter user_name:")
city = input("enter city name:")

print(name ,"lives in", city)

#5.Use the sep parameter in print() to print Python*is*fun (three separate words joined by *).
print("python","is","fun",sep="*")

