import matplotlib.pyplot as plt

categories = ["A", "B", "C", "D"]
values = [12, 19, 7, 15]

plt.bar(categories, values)
plt.xlabel("Category")
plt.ylabel("Value")
plt.title("Sample Bar Diagram")
plt.savefig("bar.png")
plt.close()
