import matplotlib.pyplot as plt
import numpy as np

# Data Structure
List = [1, 2, 3]  # Changeable , Orderable , Repeatable
Dict = {"one": 1, "two": 2, "three": 3}  # Keyable , Changeable , Orderable , Repeatable
Tuple = (1, 2, 3)  # Orderable , Repeatable
Set = {1, 2, 3}  # Changeable

# Type of Matplotlib - > 1- HighLevel , 2- OOP

# -- SimpleGrid

# Highlevel :

x = np.linspace(-10, 10, 20)
y = abs(x)
z = y + 3

plt.plot(x, z,
         label="Graph",
         color="blue",
         linestyle="-",
         )
plt.plot(x, y,
         label="Graph",
         color="black",
         marker="o",
         linestyle="--",
         )
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True, ls="--")
plt.legend(loc="upper center")

plt.title("This Is Title",
          fontsize=11,
          fontweight="bold",
          color="black",
          )
plt.show()
plt.savefig("test.png", dpi=100)

# OOP :
fig, ax = plt.subplots()

ax.plot(x, y ** 3,
        marker='o',
        color='green',
        linestyle='-.',
        )

plt.show()

# -- Bar

# HL :

Country = ["Iran", "USA", "German", "Israel"]
GDP = np.random.default_rng().integers(low=0, high=100, size=len(Country))

bars = plt.bar(Country, GDP)  # bar -> vertical,barh -> horizontal
bars[0].set_color('red')
bars[1].set_hatch("/")
bars[1].set_color('darkblue')
bars[2].set_color('orange')
bars[3].set_color('blue')
plt.show()

# OOP :

fig, ax = plt.subplots()

ax.bar(Country, GDP)
plt.show()

# -- Pie

Pop = np.random.default_rng().integers(low=1, high=100, size=len(Country))

# -- HL :
plt.figure(figsize=(8, 8))
plt.pie(Pop, labels=Country,
        explode=[0, 0, 0, 0.1],  # for apart
        colors=["gray", "blue", "orange", "lightblue"])
plt.show()

# -- OOP :


Circle = plt.Circle((0, 0), 0.1,
                    color="white")

fig, ax = plt.subplots()

ax.pie(Pop,
       labels=Country,
       autopct="%1.1f%%",
       shadow=True,
       startangle=90,
       )
ax.add_artist(Circle)  # -> Make a donat
plt.show()

# -- Fill Between
# HL :
x = np.arange(0, 10, 2)
y1 = x ** 2
y2 = x ** 3

plt.plot(x, y1)
plt.plot(x, y2)
fill = plt.fill_between(x=x,
                        y1=y1,
                        y2=y2,
                        color="skyblue",
                        alpha=0.5)

plt.show()
# OOP :
fig, ax = plt.subplots()

ax.fill_between(x=x, y1=y1, y2=y2,
                color="skyblue",
                alpha=0.5)
ax.annotate("%x^2%",
    xy=(3.5, 12),
    xytext=(3, 1),
    arrowprops=dict(arrowstyle="->"))
plt.show()
