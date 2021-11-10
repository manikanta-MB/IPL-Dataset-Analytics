""" This program shows the bar chart of total runs scored by each bangalore batsman over IPL history"""

# importing all the required libraries to deal with csv files and to plot the data.
import csv
from matplotlib import pyplot as plt
import os

# Creating the data of total runs scored by each bangalore batsman over IPL history, from scratch data.
batsman_and_score={}
with open(os.getcwd()+"/../Data/deliveries.csv","r") as f:
    reader = csv.reader(f)
    next(reader,None) # skipping the headers
    for row in reader:
        batting_team = row[2]
        if(batting_team == "Royal Challengers Bangalore"):
            batsman = row[6]
            score = int(row[15])
            batsman_and_score[batsman] = batsman_and_score.get(batsman,0) + score

# Creating X-axis and Y-axis values to define the bar chart
x_axis_values,y_axis_values = [],[]
for batsman,score in batsman_and_score.items():
    x_axis_values.append(batsman)
    y_axis_values.append(score)

# Creating and displaying the bar chart
fig = plt.figure()
fig.set_figheight(50)
fig.set_figwidth(15)
ax = fig.add_subplot(111)
ax.barh(x_axis_values,y_axis_values)
plt.ylabel("Bangalore Batsmen",fontweight='bold',fontsize=20)
plt.xlabel("Total Score Over IPL History",fontweight='bold',fontsize=20)
plt.title("Total Score by Each Bangalore batsman Over IPL History",fontweight='bold',fontsize=20)
plt.show()