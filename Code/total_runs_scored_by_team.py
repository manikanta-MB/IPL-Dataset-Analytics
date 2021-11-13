""" This program shows the bar chart of total runs scored by each team over IPL history"""

# importing all the required libraries to deal with csv files and to plot the data.
import csv
import os
from matplotlib import pyplot as plt

def get_total_runs_scored(file_path):
    """It will create and return the data of total runs scored by each team
     over IPL history, from scratch data file.
     """
    teams_and_score={}
    with open(file_path,"r",encoding="utf8") as file_obj:
        ball_delivery_reader = csv.DictReader(file_obj)
        for current_delivery_info in ball_delivery_reader:
            batting_team = current_delivery_info["batting_team"]
            total_runs = int(current_delivery_info["total_runs"])
            teams_and_score[batting_team] = teams_and_score.get(batting_team,0) + total_runs
    # deleting the duplicate team "Rising Pune Supergiant"
    rising_pune_supergiant_score = teams_and_score.get('Rising Pune Supergiant',0)
    total_score = teams_and_score.get('Rising Pune Supergiants',0) + rising_pune_supergiant_score
    teams_and_score['Rising Pune Supergiants'] = total_score
    if 'Rising Pune Supergiant' in teams_and_score:
        del teams_and_score['Rising Pune Supergiant']
    return teams_and_score

def plot_data(teams_and_score):
    """It will create and display the Bar Chart"""
    # Creating X-axis and Y-axis values to define the bar chart
    x_axis_values,y_axis_values = [],[]
    for team,score in teams_and_score.items():
        x_axis_values.append(team)
        y_axis_values.append(score)
    # Creating and displaying the bar chart
    fig = plt.figure()
    fig.set_figheight(15)
    fig.set_figwidth(15)
    fig_obj = fig.add_subplot(111)
    fig_obj.barh(x_axis_values,y_axis_values)
    plt.ylabel("IPL Teams",fontweight='bold',fontsize=20)
    plt.xlabel("Total Score Over IPL History",fontweight='bold',fontsize=20)
    plt.title("Total Score by Each Team Over IPL History",fontweight='bold',fontsize=20)
    plt.show()

def execute():
    """It will call all the helper functions to achieve our aim"""
    file_path = os.getcwd()+"/../Data/deliveries.csv"
    teams_and_score = get_total_runs_scored(file_path)
    plot_data(teams_and_score)

execute()
