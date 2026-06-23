import matplotlib.pyplot as plt

# Data
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
study_hours = [2, 3, 4, 1, 5]

# Plot graph
plt.plot(days, study_hours, marker='o')

# Title
plt.title("My Study Hours")

# Labels
plt.xlabel("Days")
plt.ylabel("Hours")

# Show graph
plt.show()