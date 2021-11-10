"""
This Program displays the Stacked bar chart for the no.of matches played by each
team in each IPL Season.
To solve this problem first i divided it into 3 modules.
    1.getting no.of matches played by each team seasonwise (but not ordered in ascending order of season year)
    2.ordering the data(got in 1st module) in ascending order of season year.
    3.Plotting the data(got in 2nd module) with the help of matplotlib library.
"""
# importing the required libraries to deal with csv files and to plot the data.
import csv
from matplotlib import pyplot as plt

# Creating the data of no.of matches played by each team in each season, from scratch data.
def get_team_season_matches(filename):
    team_season_matches={}
    seasons = set()
    with open(filename,"r") as f:
        reader = csv.reader(f)
        next(reader,None) # skipping the headers
        for row in reader:
            season = int(row[1].strip())
            seasons.add(season)
            team1 = row[4].strip()
            team2 = row[5].strip()
            if(team1 not in team_season_matches):
                team_season_matches[team1] = {}
            team_season_matches[team1][season] = team_season_matches[team1].get(season,0)+1
            if(team2 not in team_season_matches):
                team_season_matches[team2] = {}
            team_season_matches[team2][season] = team_season_matches[team2].get(season,0)+1
    seasons = sorted(list(seasons))
    return team_season_matches,seasons

# ordering the teams and correpsonding no.of matches by Seasonwise
def order_matches_seasonwise(team_season_matches,seasons):
    teams_and_matches_seasonwise = {}
    for team in team_season_matches.keys():
        teams_and_matches_seasonwise[team]=[]
        for season in seasons:
            teams_and_matches_seasonwise[team].append(team_season_matches[team].get(season,0))
    return teams_and_matches_seasonwise

# Plotting the Sorted data
def plot_the_data(teams_and_matches_seasonwise,seasons):
    no_seasons = len(seasons)
    prev_list = [0]*no_seasons # it will be useful for calculating the ending position of the previous bar.
    fig = plt.figure()
    fig.set_figheight(12)
    fig.set_figwidth(12)
    ax = fig.add_subplot(111)
    # Shrink current axis by 20%
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    # Creating the bar and Placing it to the right of previous team bar in each season.
    for team in teams_and_matches_seasonwise:
        current_team_matches = teams_and_matches_seasonwise[team]
        ax.barh(seasons,current_team_matches,left=prev_list,label = team)
        prev_list = [prev_list[i]+current_team_matches[i] for i in range(no_seasons)]
    plt.title("Number of matches played by each team Seasonwise",fontweight='bold',fontsize=20)
    plt.ylabel("Seasons",fontweight='bold',fontsize=15)
    plt.xlabel("number of matches played",fontweight='bold',fontsize=15)
    # Put a legend to the right of the current axis
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()

# Calling helper functions to extract the required data, to sort it based on season wise and to plot the result.
team_season_matches,seasons = get_team_season_matches("IPL-Dataset-Analytics/Data/matches.csv")
teams_and_matches_seasonwise = order_matches_seasonwise(team_season_matches,seasons)
plot_the_data(teams_and_matches_seasonwise,seasons)
