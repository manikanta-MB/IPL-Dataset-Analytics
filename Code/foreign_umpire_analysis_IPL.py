""" This program shows the bar chart of number of Umpires in IPL, Country wise"""

# importing all the required libraries to deal with csv files and to plot the data.
import csv
import os
from matplotlib import pyplot as plt

def get_no_of_umpires_by_country(file_path):
    """It will create a dictionary that maps country to
     number of Umpires in IPL.
    """
    umpires = {}
    with open(file_path,"r",encoding="utf8") as file_obj:
        umpires_reader = csv.DictReader(file_obj)
        for current_umpire_info in umpires_reader:
            country = current_umpire_info[" country"].strip()
            if country != "India":
                umpires[country] = umpires.get(country,0) + 1
    return umpires

def plot_data(umpires):
    """It will create and display the Bar Chart"""
    # Creating X-axis and Y-axis values to define the bar chart
    x_axis_values,y_axis_values = [],[]
    for country,count in umpires.items():
        x_axis_values.append(country)
        y_axis_values.append(count)

    # Creating and displaying the bar chart
    figure_width,figure_height = 10,10
    plt.figure(figsize=(figure_width,figure_height))
    plt.bar(x_axis_values,y_axis_values)
    plt.title("Number of Umpires in IPL Country wise",fontweight='bold')
    plt.xlabel("Country",fontweight='bold')
    plt.ylabel("Number of Umpires",fontweight='bold')
    plt.show()

def execute():
    """It will call all the helper functions to achieve our aim"""
    file_path = os.getcwd()+"/../Data/umpires.csv"
    umpires = get_no_of_umpires_by_country(file_path)
    plot_data(umpires)

execute()
