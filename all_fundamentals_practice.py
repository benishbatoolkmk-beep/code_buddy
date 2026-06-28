#-----------------------------Task 1: Student Grade Calculator------------------------------

#Take a student's name and marks for 3 subjects as input. Calculate the average, then decide a grade (A/B/C/Fail). Write everything inside a function that returns the name, average, and grade.
def calculate_grades():
    student_name = input("enter your name:")
    marks1 = int(input("enter your marks:"))
    marks2 = int(input("enter your marks:"))
    marks3 = int(input("enter your marks:"))
    average = (marks1 + marks2 + marks3) / 3
    if average >= 90:
        grades = "A" 
    elif average >=80:
        grades = "B"
    elif average >= 70:
        grades = "C"
    elif average >= 60:
       grades = "D"
    else:
        grades = "F"
    return student_name , average , grades 
student_name , average , grades = calculate_grades()
print(student_name,"got average:",average,"grades:" ,grades)


#------------------------------------Task 2: Shopping Cart----------------------------------

#Create an empty list called "cart". Ask the user for an item name 5 times (using a loop), and append each item to the list. After the loop, print the full list and show the total number of items (using len()).
cart = []
for i in range(5):
    item = input("enter item name:")
    cart.append(item)

print(cart)
print("total items:",len(cart))


#---------------------------------Task 3: Word Frequency Counter----------------------------

#Take a sentence string (e.g. "the quick brown fox jumps over the the lazy dog the"). Split it into words using .split(). Create a dictionary that counts how many times each word appears. Use a loop to count, then print which word appeared the most.
sentence = str("the quick brown fox jumps over the lazy dog the.")
words = sentence.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] = word_count[word]+ 1
    else:
        word_count[word] = 1 
most_common_word = max(word_count, key=word_count.get)
print(most_common_word)

#------------------------------------Task 4: Even/Odd Separator------------------------------
#Take a list numbers = [1,2,3,4,5,6,7,8,9,10]. Loop through it and check if each number is even or odd. Create two separate lists — evens and odds — and append numbers to them accordingly. Print both final lists.
numbers = [1,2,3,4,5,6,7,8,9,10]
evens = []
odd = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    else:
        odd.append(num)
print("evens:",evens)
print("odd:",odd)

#------------------------------Task 5: Simple Login System----------------------------------
#Create a dictionary of username-password pairs (e.g. {"sundas": "1234", "ali": "abcd"}). Take a username and password as input. Check if the username exists and the password matches. If yes, print "Login successful", otherwise print "Invalid credentials".
users = {"sundas": "1234", "ali": "abcd"}
username = input("enter a username:")
password = input("enter your password:")

if username in users and users[username] == password:
    print("login successfull")
else:
    print("login failed")
        




