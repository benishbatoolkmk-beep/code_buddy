import matplotlib
print(matplotlib.__version__)
#Matplotlib Pyplot
import matplotlib.pyplot as plt
# Create some data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
# Create a line plot
plt.plot(x, y)
# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot Example')
# Show the plot
plt.show()
#example
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()
#Markers
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints, marker = 'o')
plt.show()
#Marker size
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints, marker = 'o', markersize = 10)
plt.show()
#Marker color
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints, marker = 'o', markerfacecolor = 'red')
plt.show()
#Matplotlib Line
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints, linestyle = 'dashed')
plt.show()
#Line color
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints, linestyle = 'dashed', color = 'green')
plt.show()
