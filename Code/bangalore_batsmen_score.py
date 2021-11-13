"""This program shows the bar chart of Top 10 bangalore batsmen
over IPL history
"""

# importing all the required libraries to deal with csv files and to plot the data.
import csv
import os
from matplotlib import pyplot as plt

def get_bangalore_batsmen_and_score(file_path):
    """It will create and return a dictionary that maps each bangalore
     batsman to their corresponding score over IPL History.
    """
    batsman_and_score={}
    with open(file_path,"r",encoding="utf8") as file_obj:
        ball_delivery_reader = csv.DictReader(file_obj)
        for current_delivery_info in ball_delivery_reader:
            batting_team = current_delivery_info["batting_team"]
            if batting_team == "Royal Challengers Bangalore":
                batsman = current_delivery_info["batsman"]
                score = int(current_delivery_info["batsman_runs"])
                batsman_and_score[batsman] = batsman_and_score.get(batsman,0) + score
    return batsman_and_score

def get_top_10_batsmen(batsman_and_score):
    """It will fetch the top 10 batsmen names based on their score"""
    batsmen_names = list(batsman_and_score.keys())
    batsmen_names.sort(key=lambda name:batsman_and_score[name],reverse=True)
    top_10_batsmen_names = batsmen_names[:10][::-1]
    return top_10_batsmen_names

def plot_data(batsman_and_score,top_10_batsmen_names):
    """It will create and display the bar chart"""
    # Creating X-axis and Y-axis values to define the bar chart
    x_axis_values,y_axis_values = [],[]
    for batsman_name in top_10_batsmen_names:
        score = batsman_and_score[batsman_name]
        x_axis_values.append(batsman_name)
        y_axis_values.append(score)

    # Creating and displaying the bar chart
    figure_width,figure_height = 15,15
    plt.figure(figsize=(figure_width,figure_height))
    plt.barh(x_axis_values,y_axis_values)
    plt.ylabel("Batsman name",fontweight='bold')
    plt.xlabel("Total Score Over IPL History",fontweight='bold')
    plt.title("Top 10 Bangalore batsmen Over IPL History",fontweight='bold',fontsize=20)
    plt.show()

def execute():
    """It will call all the helper functions to achieve our aim"""
    file_path = os.getcwd()+"/../Data/deliveries.csv"
    batsman_and_score = get_bangalore_batsmen_and_score(file_path)
    top_10_batsmen_names = get_top_10_batsmen(batsman_and_score)
    plot_data(batsman_and_score,top_10_batsmen_names)

execute()
