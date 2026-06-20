#1.Create variables for your name, age, and is_employed (True/False), then print all three.
name = "sundas safder"
age = 23
is_employed = False
print(name,age,is_employed)

#2.Create three variables a, b, c all in one line with values 5, 10, 15.
a , b , c = 5,10,15
print(a,b,c)

#3.Create one variable called temperature, assign it an integer, print its type(), then reassign it a string value and print its type() again to see it change.
temperature = 20
print(type(temperature))

temperature = "cold"
print(type(temperature))

#4.Create two variables first_name and last_name. Combine (concatenate) them to create a full_name variable and print it.
first_name = "sundas"
last_name = "safder ali"
print(first_name+last_name)

#5.Create num1 = 10 and num2 = 3. Swap their values (so num1 gets num2's value and vice versa) without using a third variable. Print both to check.
num1 = 10
num2 = 3 
num1 , num2 = num2 , num1
print(num1)
print(num2)

#6.Create a = 7 and b = 2. Add, subtract, multiply, and divide them, storing results in 4 separate variables (sum_result, sub_result, mul_result, div_result). Print all of them.
a = 7
b = 2 
sum_results = a + b 
sub_results = a - b 
mul_results = a * b 
div_results = a / b 
print(sum_results)
print(sub_results)
print(mul_results)
print(div_results)

#Create a variable mixed = 42. Print type(mixed). Then reassign mixed = 42.5, print type() again. Then reassign mixed = "42", print type() again. Observe how the output changes each time.
mixed = 42
print(type(mixed))
mixed = 42.5
print(type(mixed))
mixed = 42
print(type(mixed))


