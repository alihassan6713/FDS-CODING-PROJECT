

# Importing the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read data from file
data = pd.read_csv("data2.csv")

# Calculate average weight
avg_weight = data.mean().values[0]

# Printing the value
print("Average Newborn Weight: ", avg_weight)

# Calculate fraction of babies born with weights between average and 1.2 times average
mask = (data >= avg_weight) & (data <= 1.2 * avg_weight)
X = np.count_nonzero(mask) / len(data)

# Printing the value
print("Fraction of babies born with weights between average and 1.2 times average: ", X)

# Creating histogram
plt.hist(data, bins=20, orientation='horizontal', histtype='bar', color='g', edgecolor='y', label='total baby weights')
plt.axhline(y=avg_weight, color='b', linestyle='-', label='W')
plt.axhline(y=X, color='r', linestyle='-', label='X')

# Adding the label on X axis and Y axis
plt.ylabel('Weight (lbs)')
plt.xlabel('Count')

# Adding the title
plt.title('Newborn Weight Distribution')

# Adding legend
plt.legend()

# Plotting the Grid
plt.grid(True)

# Show plot
plt.show()
