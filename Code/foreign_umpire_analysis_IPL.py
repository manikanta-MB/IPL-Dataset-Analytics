""" This program shows the bar chart of number of Umpires in IPL, Country wise"""

# importing all the required libraries to deal with csv files and to plot the data.
import csv
import os
from matplotlib import pyplot as plt

# Creating the data of number of Umpires country wise, from scratch data.
umpires = {}
with open(os.getcwd()+"/../Data/umpires.csv","r",encoding="utf8") as f:
    reader = csv.reader(f)
    next(reader,None) # skipping the headers
    for row in reader:
        country = row[1].strip()
        if country != "India":
            umpires[country] = umpires.get(country,0) + 1

# Creating X-axis and Y-axis values to define the bar chart
x_axis_values,y_axis_values = [],[]
for country,count in umpires.items():
    x_axis_values.append(country)
    y_axis_values.append(count)

# Creating and displaying the bar chart
fig = plt.figure()
fig.set_figheight(10)
fig.set_figwidth(10)
ax = fig.add_subplot(111)
ax.bar(x_axis_values,y_axis_values)
plt.title("Number of Umpires in IPL Country wise",fontweight='bold')
plt.xlabel("Country",fontweight='bold')
plt.ylabel("Number of Umpires in IPL",fontweight='bold')
plt.show()
