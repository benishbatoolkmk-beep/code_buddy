#1.Create a list numbers = [10, 20, 30, 40, 50]. Print the first item and the last item (use negative indexing for the last one).
numbers = [10,20,30,40,50]
print(numbers[0])
print(numbers[4])
print(numbers[-1])

#2.Create a list colors = ["red", "blue", "green"]. Add "yellow" to it, then print the whole list.
colors = ["red","blue","green"]
colors.append("yellow")
print(colors)

#3.Create a list [5, 3, 8, 1, 9], sort it using .sort(), and print it.
list = [5,3,8,1,9]
list.sort()
print(list)

#4.Use a for loop to find the sum of all numbers in the list [1, 2, 3, 4, 5] (add them up using a variable as you loop), and print the total.
total = 0
list = [1,2,3,4,5]
for lis in list:
    total = total + lis
print(total)

#5.Create a list fruits = ["apple", "banana", "mango", "orange"]. Use a loop to check which fruit names have more than 5 letters, and print only those.
fruits = ["apple", "banana", "mango", "orange"]
for fruit in fruits:
    if len(fruit) >5:
        print(fruit) 


#--------------------------------------DICTIONARY-------------------------------------------
#1.Create a dictionary person = {"name": "Ali", "age": 30}. Print the values of name and age.
person = {"name": "ali",
          "age": 30,
         }
print(person["name"])
print(person["age"])

#2.Add a new key "city" with value "Karachi" to the person dictionary, then print the whole dictionary.
person = {"name": "ali",
          "age": 30
          }
person["city"] = "karachi"
print(person)

#3.Create a dictionary {"a": 1, "b": 2, "c": 3}. Use a loop to print all keys and values (in key : value format).
dic = {"a": 1 ,
       "b": 2 ,
       "c": 3
       }
for key,value in dic.items():
    print(key ,":", value )

#4.Create a dictionary marks = {"math": 90, "english": 85, "science": 95}. Use a loop to check which subjects have marks greater than 88, and print only those.
marks = {"math": 90, "english": 85, "science": 95}
for subject,score in marks.items():
    if score > 88:
        print(marks)

#5.In the dictionary person = {"name": "Sara", "age": 25}, check whether the "age" key exists (using in), and print the result.
person = {"name": "Sara", "age": 25}
if "age" in person:
    print("yes, age key exist")
else:
    print("no")


#--------------------------------------------TUPLE AND SET----------------------------------
#1.Create a tuple days = ("Mon", "Tue", "Wed"). Print the first and last item.
days = ("mon","tus","wed")
print(days[0])    
print(days[1])

#2.Try colors[0] = "green" on a tuple colors = ("red", "blue") — observe the exact error message and understand why it happens.
#colors = ("red", "blue") 
#colors[0] = "green"
#print(colors)              #tuple does not support item assignment

#3.Create a set Create a set numbers = {1, 2, 2, 3, 3, 4}, print it, and see how the duplicates disappear., print it, and see how the duplicates disappear.
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)


#4.Convert the list [1, 1, 2, 3, 3, 3, 4, 5, 5] into a set and print the unique values.
numbers_list = [1, 1, 2, 3, 3, 3, 4, 5, 5]
unique_numbers = set(numbers_list)
print(unique_numbers)

#5.Create a set Create a set fruits = {"apple", "banana", "mango"}. Add "orange" to it, then remove "banana", and print the final set.. Add "orange" to it, then remove "banana", and print the final set.
fruits = {"apple", "banana", "mango"}
fruits.add("orange")
fruits.remove("banana")
print(fruits)



