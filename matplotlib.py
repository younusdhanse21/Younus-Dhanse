
import matplotlib.pyplot as plt
import numpy as np

# Line Plot
x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x), label="sin(x1)")
plt.plot(x, np.cos(x), label="cos(x)")


plt.title("Trigonometric Functions")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(False)
plt.show()

# Bar Chart
categories = ["Python", "Java", "C++", "JS"]
popularity = [35, 20, 15, 30]
plt.bar(categories, popularity,
color=["#306998","#f89820",
"#00599C","#f7df1e"])
plt.title("Language Popularity")
plt.ylabel("Percentage (%)")
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Scatter Plot
np.random.seed(42)
x = np.random.randn(100)
y = 2*x + np.random.randn(100)*0.5
plt.scatter(x, y, alpha=0.6, c=y,
cmap="viridis")
plt.colorbar(label="Value")
plt.title("Scatter Plot with Colormap")
plt.show()

# Pie Chart
sizes = [40, 25, 20, 15]
labels = ["AI/ML", "Web Dev",
"Data Science", "Other"]
plt.pie(sizes, labels=labels,
autopct="%1.1f%%", startangle=90,
explode=(0.05, 0, 0, 0))
plt.title("Python Usage by Domain")
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Histogram
data = np.random.normal(70, 10, 1000)
plt.hist(data, bins=30, edgecolor="black",
alpha=0.7, color="#306998")
plt.title("Exam Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.axvline(data.mean(), color="red",
linestyle="--", label="Mean")
plt.legend()
plt.show()

# Box Plot
scores = [np.random.normal(m, 8, 50)
for m in [65, 72, 80, 68]]
plt.boxplot(scores,
labels=["Q1","Q2","Q3","Q4"])
plt.title("Quarterly Performance")
plt.ylabel("Score")
plt.show()


import seaborn as sns
import pandas as pd
import numpy as np

# Heatmap (correlation matrix)
df = pd.DataFrame(
np.random.randn(100, 4),
columns=["Math","Science","English","Art"]
)
corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm",
center=0, square=True)
plt.title("Subject Correlation Heatmap")
plt.show()

# Seaborn styles
sns.set_theme(style="whitegrid")

# Distribution plot
tips = sns.load_dataset("tips")
sns.histplot(tips["total_bill"], kde=True)
plt.title("Bill Distribution")
plt.show()

# Category plot
sns.boxplot(x="day", y="total_bill",
data=tips, palette="Set2")
plt.title("Bills by Day")
plt.show()


