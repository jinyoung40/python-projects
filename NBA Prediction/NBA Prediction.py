import pandas as pd

dffm = pd.read_csv("NBA Finals and MVP.csv", encoding = 'unicode_escape')
dffm = dffm[["Year", "Western Champion", "Eastern Champion", "NBA Champion", "NBA Vice-Champion","MVP Name","MVP Position", "MVP Team", "MVP Nationality", "MVP status"]]
dffm.columns = ["Year", "West Champ", "East Champ", "NBA Champ", "Runnerup", "MVP", "Position", "Team", "National", "Status"]


dfhist = pd.read_csv("Seasons_Stats.csv")
dfhist = dfhist[["Year", "Player", "Pos", "Tm", "G", "MP", "PER", "TS%", "OWS", "DWS", "WS", "WS/48", "BPM", "VORP", "FGA", "FG%", "3P","3PA","3P%", "2P", "2PA", "2P%", "TRB", "AST", "STL", "BLK", "TOV", "PTS" ]]
dfhist.columns = ["Year", "Name", "Position", "Team", "Game Played", "Minutes", "PER", "True Shooting", "OWinshare", "DWinshare", "Winshare", "Winshare/48", "BPM", "VORP", "FGA", "FG%","3P","3PA","3P%", "2P", "2PA", "2P%", "Rebound", "Assist", "Steal", "Block", "Turnover", "Point" ]

#How many teams with MVP won/not won conference championship and NBA championship
print("Teams with MVP and their championship")
print("================================================================================")
dffm["Team"] = dffm["Team"].fillna("None")
dffmm = dffm[dffm["Team"] != "None"] #cleaning up the file

cchamp = len(dffmm[(dffmm["Status"] == "Champion") | (dffmm["Status"] == "Vice-Champion")]) #at least win conference
fchamp = len(dffmm[(dffmm["Status"] == "Champion")]) #win final championship

print("Out of ", len(dffmm), "MVPs, ", cchamp, "MVP was at least won their conference.","(", cchamp/len(dffmm)*100, "% )")
print("Out of ", len(dffmm), "MVPs, ", fchamp, "MVP was won NBA Championship.","(", fchamp/len(dffmm)*100, "% )")
aa = input("Press Enter To Continue")

#Team with most MVP vs team with most championship
print("\n")
print("Team with most MVP and most championship")
print("===============================================")
mvps = dffmm.groupby("Team")["Year"].count().nlargest(3).reset_index() # top 3 teams with most number of mvps
teams = dffmm.groupby("NBA Champ")["Year"].count().nlargest(3).reset_index() #top 3 teams with most number of championship
print("1. Top 3 teams with most number of MVPs", "\n", mvps)
print("\n")
print("2. Top 3 teams with most number of NBA Championship", "\n",teams)
ab = input("Press Enter To Continue")

#MVP by position GROUP BY era (1970s, 1980s etc) 
print("\n")
print("MVP by position GROUP BY era")
print("=================================================")
y = dffmm.groupby(["Year"]).count().reset_index()["Year"].tolist() #creating list of years
years = [y[10],y[20], y[30], y[40], y[50], y[61]]

tposi = dffmm.groupby("Position")["Year"].count().nlargest(3).reset_index() #total number of position winning mvps
print("1. Total MVP By Position","\n", tposi,"\n")
ac = input("Press Enter To Continue")

print("2. MVP by position each decade")
import matplotlib.pyplot as plt
guard = []
forward = []
center = []

for year in years:
    dffmy = dffm[(dffm["Year"] >= year-10) & (dffm["Year"] < year)] #to get data for every 10 years
    posi = dffmy.groupby("Position")["Year"].count().nlargest(3).reset_index()
    
    pguard = dffmy[(dffmy["Position"]=="Guard")]
    pforward = dffmy[(dffmy["Position"]=="Forward")]
    pcenter = dffmy[(dffmy["Position"]=="Center")]
    guard.append(len(pguard))
    forward.append(len(pforward))
    center.append(len(pcenter))

d = pd.DataFrame({"Center": center, "Forward": forward, "Guard": guard}, index = years)
a = d.plot.bar(rot=0)
plt.show()
ad = input("Press Enter To Continue")

print("\n")
print("Trend Analysis")
print("=======================")

ddhist = dfhist[dfhist["Year"] >= 1980] #only need year after 1980: three points rule created & can be changed based on user preference

years = ddhist.groupby(["Year"]).count().reset_index()["Year"].tolist()
threepdata = []
twopdata = []

for year in years:
    
    totalfa = ddhist.loc[ddhist["Year"] == year, "FGA"].sum() #total field goal attempts each year
    
    threepa = ddhist.loc[ddhist["Year"] == year, "3PA"].sum() #total 3 point attempts each year
    threepdata.append(threepa/totalfa)                        #percentage of 3 points over total fg attempts
    
    twopa = ddhist.loc[ddhist["Year"] == year, "2PA"].sum()  #total 2 point attempts each year
    twopdata.append(twopa/totalfa)                           #percentage of 2 points over total fg attempts

print("1. Three Points Attempt Trend")
import matplotlib.pyplot as plt
plt.plot(years,threepdata)
plt.show()

print("=================================================")

print("\n")
print("2. Two Points Attempt Trend")
import matplotlib.pyplot as plt
plt.plot(years,twopdata)
plt.show()
ae = input("Press Enter To Continue")

print("=================================================")
# Advanced stats by position
ddhist = dfhist[dfhist["Year"] >= 2005]  #to find recent trends and year can be changed to based on user preference
years = ddhist.groupby(["Year"]).count().reset_index()["Year"].tolist()


#A Win Share is worth one-third of a team win. Win Shares are assigned to players based on their offense, defense, and playing time. 
#If a team wins 60 games, there are 180 Win Shares to distribute among the players. This is always true; if a team wins n games, 
#then there are 3n Win Shares to allocate to the players.

winsharelist = ddhist.nlargest(50, "Winshare") #the sabermetrics can be changed to any statistic user wants to know
print("\n")
print("3. <Stat = Winshare : Top 50 players' position from 2005>")
print(winsharelist.groupby("Position")["Year"].count().sort_values(ascending = False),"\n")

import matplotlib.pyplot as plt
winsharelist.groupby(["Year", "Position"]).size().unstack().plot(kind='bar',stacked=True)
plt.show()
print("=================================================")
af = input("Press Enter To Continue")

print("\n")
print("4. <Stat = Winshare : Top 10 players' position each year from 2005>")
big = []
small = []

for year in years: 
    ddfhist = ddhist[(ddhist["Year"] == year)]
    wslist = ddfhist.nlargest(10, "Winshare") #top 10 player with highest winshare/48 each year
    wsbig = wslist[(wslist["Position"]=="C") | (wslist["Position"]=="PF")] #categorize big (C, PF) vs small (G, SF)
    wssmall = wslist[(wslist["Position"]!="C") & (wslist["Position"]!="PF")]
    big.append(len(wsbig))
    small.append(len(wssmall))

dff = pd.DataFrame({"C & PF": big, "PG & SG & SF": small}, index = years)
axx = dff.plot.bar(rot=0)
plt.show()
print("=================================================")
ag = input("Press Enter To Continue")


#Value over Replacement Player (VORP): VORP is defined by Basketball Reference as a measure to estimate each player’s overall 
#contribution to the team, measured vs. what a theoretical “replacement player” would provide, where the “replacement player” is 
#defined as a player on minimum salary or not a normal member of a team’s rotation.

vorplistt = ddhist.nlargest(50, "VORP")
print("\n")
print("5. <Stat = VORP : Top 50 players' position from 2005>")
print(vorplistt.groupby("Position")["Year"].count().sort_values(ascending = False),"\n")

import matplotlib.pyplot as plt
vorplistt.groupby(["Year", "Position"]).size().unstack().plot(kind='bar',stacked=True)
plt.show()
print("=================================================")
ah = input("Press Enter To Continue")
print("\n")
print("6. <Stat = VORP : Top 10 players' position each year from 2005>")
bigman = []
smallman = []
for year in years:
    ddffhist = ddhist[(ddhist["Year"] == year)]
    vorplist = ddffhist.nlargest(10, "VORP")
    vorpbig = vorplist[(vorplist["Position"]=="C") | (vorplist["Position"]=="PF")]
    vorpsmall = vorplist[(vorplist["Position"]!="C") & (vorplist["Position"]!="PF")]
    bigman.append(len(vorpbig))
    smallman.append(len(vorpsmall))

df = pd.DataFrame({"C & PF": bigman, "PG & SG & SF": smallman}, index = years)
ax = df.plot.bar(rot=0)
plt.show()

ai = input("Press Enter To Continue")
#Playoff Prediction
print("\n")
print("=================================================")
print("<Playoff prediction>")

import pandas as pd
import matplotlib.pyplot as plt  # To visualize
from sklearn.linear_model import LinearRegression

df =  pd.read_csv('NBA_data1.csv')

# Points difference
PTSdiff = df['PTS'] - df['oppPTS']
Win = df['W']

# Check for linear relationship between Win and Points Difference
plt.scatter(PTSdiff, Win, color='blue')
plt.xlabel("Point Difference")
plt.ylabel("Win")
plt.show()
input("Press Enter To Continue")

# Add Point Difference to the data frame
df['PTSdiff'] = PTSdiff  

X = df.iloc[:, 20].values.reshape(-1, 1)  # values converts it into an array
Y = df.iloc[:, 3].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column

# Linear regression model for wins
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X, Y)  # perform linear regression
Y_pred = linear_regressor.predict(X)  # make predictions

plt.scatter(X, Y, color='blue')
plt.plot(X, Y_pred, color='red')
plt.xlabel("Point Difference")
plt.ylabel("Win")
plt.show()

input("Press Enter To Continue")

tab = df.groupby(['W', 'Playoffs']).size()
print(tab.to_string())

#playoffdf = df[df.Playoffs == 1] # find how many wins you need to go to Playoffs
#playoffdf = playoffdf.groupby("W")["Playoffs"].count()
#print(playoffdf)

#playoffdf = df[df.Playoffs == 0] # find how many wins you need to go to Playoffs
#playoffdf = playoffdf.groupby("W")["Playoffs"].count()
#print(playoffdf)

input("Press Enter To Continue")

df = df[["SeasonEnd", "Team", "Playoffs","W","PTS", "oppPTS", "FG", "2P" ,"3P", "2PA","3PA","FT","FTA","ORB","DRB","AST", "STL", "BLK", "TOV"]]
df.columns = ["SeasonEnd", "Team", "Playoffs", "W","PTS","oppPTS","FG","X2P","X3P","X2PA","X3PA","FT","FTA","ORB","DRB","AST","STL","BLK","TOV"]


import statsmodels.formula.api as smf

print("")
print("Model 1 ++++++++++==============")
model = smf.ols(formula='Win ~ PTSdiff', data=df)
res = model.fit()
print(res.summary())
print("")

input("Pres Enter to Continue")
print("y_predict = 0.0326*x + 41")

xM1 = input('Enter Ave. Point Differece:')
yM1 = 0.0326*int(xM1) + 41
print(yM1)
input("Press Enter To Continue")

print("Model 2 +++++++++++===========")
model2 = smf.ols(formula='PTS ~ X2PA + X3PA + FTA + ORB + AST  +STL', data=df)
res2 = model2.fit()
print(res2.summary())