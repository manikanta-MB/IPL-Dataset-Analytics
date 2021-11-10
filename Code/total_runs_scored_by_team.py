""" This program shows the bar chart of total runs scored by each team over IPL history"""

# importing all the required libraries to deal with csv files and to plot the data.
import csv
from matplotlib import pyplot as plt

# Creating the data of total runs scored by each team over IPL history, from scratch data.
teams_and_score={}
with open("IPL-Dataset-Analytics/Data/deliveries.csv","r") as f:
    reader = csv.reader(f)
    next(reader,None) # skipping the headers
    for row in reader:
        batting_team = row[2]
        total_runs = int(row[17])
        teams_and_score[batting_team] = teams_and_score.get(batting_team,0) + total_runs

# Creating X-axis and Y-axis values to define the bar chart
x_axis_values,y_axis_values = [],[]
for team,score in teams_and_score.items():
    x_axis_values.append(team)
    y_axis_values.append(score)

# Creating and displaying the bar chart
fig = plt.figure()
fig.set_figheight(15)
fig.set_figwidth(15)
ax = fig.add_subplot(111)
ax.barh(x_axis_values,y_axis_values)
plt.ylabel("IPL Teams",fontweight='bold',fontsize=20)
plt.xlabel("Total Score Over IPL History",fontweight='bold',fontsize=20)
plt.title("Total Score by Each Team Over IPL History",fontweight='bold',fontsize=20)
plt.show()