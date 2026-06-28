#1.Create a simple line chart with x = [1, 2, 3, 4, 5] and y = [2, 4, 6, 8, 10]. Add a title and axis labels.
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.title("my chart")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()

#2.Create a bar chart showing marks for 4 subjects (Math, Physics, Chemistry, Biology).
import matplotlib.pyplot as plt 
subjects = ["math","physics","chemistry","biology"]
marks = [30,40,50,60]
plt.bar(subjects,marks)
plt.show()

#3.Plot two different lines on the same chart (e.g. comparing two students' marks), and show a legend.
import matplotlib.pyplot as plt

subjects = [1, 2, 3, 4, 5]      # subject numbers (x-axis)
ali_marks = [80, 85, 78, 90, 88]
sara_marks = [75, 92, 85, 80, 95]

plt.plot(subjects,ali_marks,label="ali")
plt.plot(subjects,sara_marks, label= "sara")
plt.legend()
plt.title("marks comparison")
plt.xlabel("subjects")
plt.ylabel("marks")
plt.show()

#4.Create a pie chart showing your daily time breakdown (e.g. Sleep, Study, Phone, Other).
import matplotlib.pyplot as plt
labels = ["Sleep", "Study", "Phone", "Other"]
hours = [8, 4, 3, 9]      # total = 24
plt.pie(hours , labels=labels)
plt.title("my daily time breakdown")
plt.show()

#5.Create a scatter plot with 5-6 random x,y points, customizing color and marker.
x = [2, 4, 6, 8, 10, 12]
y = [3, 7, 2, 9, 5, 11]
import matplotlib.pyplot as plt

plt.scatter(x, y, color="red", marker="*")
plt.title("Random Points")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()