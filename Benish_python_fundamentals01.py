# my first practice with python
print("Hello World")
# this is a comment
#list
my_list = [1, 2, 3, 4, 5]
print(my_list)
# tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
# dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)
# set
my_set = {1, 2, 3, 4, 5}
print(my_set)
#conditions
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
# loops
for i in range(5):
    print(i)
while x > 0:
    print(x)
    x -= 1
# functions
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
#Git commands
# git init
Current folder ko Git repository bana deta hai.
# git add .
“Git, ye files next save (commit) me include karna.”
# git commit -m "Initial commit"
“Git, ye files ko save karna with a message describing the changes.”

# git remote add origin <repository_url>
“Git, ye remote repository ko origin naam se add karna.”
# git push -u origin master
“Git, local master branch ko remote repository ke master branch pe push karna aur origin ko track karna.”
