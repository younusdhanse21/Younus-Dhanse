
import math
sqrt_value=math.sqrt(25)
print(sqrt_value)

import math
fact=math.factorial(5)
print("factorial is",fact)

print(f"VAlue of pi",{math.pi})

import random
rand_int=random.randint(1,10)
print(f"The random value between 1-10 is",{rand_int})

my_list=["Apple","Mango","Banana"]
rand_choice=random.choice(my_list)
print(f"The random choice is,{rand_choice}")

random.shuffle(my_list)
print(f"Shuffled list: {my_list}")

import datetime
now = datetime.datetime.now()
print(f"Current date and time: {now}")

my_date=datetime.date(2023,10,26)
print(f"Specific date:{my_date}")

today=datetime.date.today()
difference=today-my_date
print(f"Days since{my_date}:{difference.days}")

import re
text = "The quick brown fox jumps over the lazy dog."
pattern = r"fox"
match = re.search(pattern, text)
if match:
    print(f"Pattern '{pattern}' found at index {match.start()} in '{text}'")

new_text = re.sub(r"lazy", "sleepy", text)
print(f"Text after replacement: {new_text}")

numbers = re.findall(r"\d+", "There are 123 apples and 45 oranges.")
print(f"Numbers found: {numbers}")

import statistics

data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
mean_value = statistics.mean(data)
print(f"Mean of data: {mean_value}")

median_value = statistics.median(data)
print(f"Median of data: {median_value}")

# Example: Calculate mode
mode_value = statistics.mode(data)
print(f"Mode of data: {mode_value}")

# Example: Calculate standard deviation
stdev_value = statistics.stdev(data)
print(f"Standard deviation of data: {stdev_value}")

import pandas as pd
import numpy as np
numpy_array = np.array([10, 20, 30, 40, 50])
print(f"NumPy array: {numpy_array}")
print(f"Sum of NumPy array elements: {np.sum(numpy_array)}")

# Pandas example: Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
display(df.head())

ages = df['Age']
print("\nAges column:")
display(ages.head())

# Pandas example: Filter data
filtered_df = df[df['Age'] > 30]
print("\nDataFrame with Age > 30:")
display(filtered_df.head())

import matplotlib.pyplot as plt
import numpy as np

# Example: Create a simple line plot
x = np.linspace(0, 10, 100) # 100 points between 0 and 10
y = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y)
plt.title('Simple Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

# Example: Create a scatter plot
n_points = 50
x_scatter = np.random.rand(n_points) * 10
y_scatter = np.random.rand(n_points) * 10

plt.figure(figsize=(8, 4))
plt.scatter(x_scatter, y_scatter, color='red', alpha=0.7)
plt.title('Random Scatter Plot')
plt.xlabel('X Value')
plt.ylabel('Y Value')
plt.grid(True)
plt.show()
