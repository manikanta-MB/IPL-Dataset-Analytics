"""
This Program displays the Stacked bar chart for the no.of matches played by each
team in each IPL Season.
To solve this problem first i divided it into 3 modules.
    1.getting no.of matches played by each team seasonwise
     (but not ordered in ascending order of season year)
    2.ordering the data(got in 1st module) in ascending order of season year.
    3.Plotting the data(got in 2nd module) with the help of matplotlib library.
"""
# importing the required libraries to deal with csv files and to plot the data.
import csv
import os
from matplotlib import pyplot as plt

def get_team_season_matches(filename):
    """Creating the data of no.of matches played by each team in
    each season, from scratch data.
    """
    with open(filename,"r",encoding="utf8") as file_obj:
        reader = csv.reader(file_obj)
        next(reader,None) # skipping the headers
        for row in reader:
            season = int(row[1].strip())
            seasons.add(season)
            team1 = row[4].strip()
            team2 = row[5].strip()
            if team1 not in team_season_matches:
                team_season_matches[team1] = {}
            team_season_matches[team1][season] = team_season_matches[team1].get(season,0)+1
            if team2 not in team_season_matches:
                team_season_matches[team2] = {}
            team_season_matches[team2][season] = team_season_matches[team2].get(season,0)+1

def order_matches_seasonwise():
    """ordering the teams and correpsonding no.of matches by Seasonwise"""
    for team,season_data in team_season_matches.items():
        teams_and_matches_seasonwise[team]=[]
        for season in seasons:
            teams_and_matches_seasonwise[team].append(season_data.get(season,0))

def plot_the_data():
    """Plotting the Sorted data"""
    no_seasons = len(seasons)
    # it will be useful for calculating the ending position of the previous bar.
    prev_list = [0]*no_seasons
    fig = plt.figure()
    fig.set_figheight(12)
    fig.set_figwidth(12)
    fig_obj = fig.add_subplot(111)
    # Shrink current axis by 20%
    box = fig_obj.get_position()
    fig_obj.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    #Hardcoding the names of colors for each team
    colors = [
                "fuchsia","maroon","red","yellow","blue","lime","purple",
                "black","green","olive","teal","aqua","navy","grey"
            ]
    # Creating the bar and Placing it to the right of previous team bar in each season.
    j=0
    for team,current_team_matches in teams_and_matches_seasonwise.items():
        fig_obj.barh(seasons,current_team_matches,left=prev_list,label = team,color=colors[j])
        prev_list = [prev_list[i]+current_team_matches[i] for i in range(no_seasons)]
        j += 1
    plt.title("Number of matches played by each team Seasonwise",fontweight='bold',fontsize=20)
    plt.ylabel("Seasons",fontweight='bold',fontsize=15)
    plt.xlabel("number of matches played",fontweight='bold',fontsize=15)
    # Put a legend to the right of the current axis
    fig_obj.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()

# Calling helper functions to extract the required data, to sort it
# based on season wise and to plot the result.
team_season_matches={}
seasons = set()
teams_and_matches_seasonwise = {}
get_team_season_matches(os.getcwd()+"/../Data/matches.csv")
seasons = sorted(list(seasons))
order_matches_seasonwise()
plot_the_data()
