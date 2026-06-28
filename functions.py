#1.Create a function square(num) that returns the square of a number.
def square(num):
    return num * num
x = square(5)
print(x)

#2.Create a function cube(num) that returns the cube of a number (number multiplied by itself 3 times). Then call it and store the result in a variable, and print that variable.
def cube(num):
    return num * num * num 
result = cube(2)
print(result)

#3.Create a function double(num) that returns the number multiplied by 2. Call it with two different numbers and print both results.
def double(num):
    return num * 2 
result1 = double(5)
result2 = double(10)
print(result1)
print(result2)

#4.Create a function add_ten(num) that returns the number plus 10. Then use the returned value in a calculation — like result = add_ten(5) then print(result * 2) — and predict the output before running it.
def add_ten(num):
    return num + 2
result = add_ten(5)
print(result * 2)

#5.Create a function is_positive(num) that returns True if the number is greater than 0, otherwise returns False. Call it with a few different numbers (positive, negative, zero) and print the results.
def is_positive(num):
    
    if num > 0:
        return True
    else:
        return False

print(is_positive(4))
print(is_positive(-6))
print(is_positive(0))