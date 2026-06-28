#1.Use a for loop to print numbers from 1 to 10.
for num in range(1,10):
    print(num)

#2.Use a for loop to print only the even numbers from 1 to 50.
for i in range(0,50,2):
    print(i)

#3.Use a while loop to count down from 5 to 0 (5, 4, 3, 2, 1, 0).
count = 5
while count >= 0:
    print(count)
    count = count - 1    

#4.Take a number from the user, and use a for loop to print its multiplication table from 1 to 10 (e.g. for 5: 5, 10, 15, ... 50).
num = int(input("enter a number:"))
for i in range(1 , 11):
    print(num, "x", i, "=", num * i)

#5.Use a for loop to print numbers from 1 to 20, but stop the loop using break when the number reaches 13.

for i in range(1, 21):
    if i == 13:
        break
    print(i)


