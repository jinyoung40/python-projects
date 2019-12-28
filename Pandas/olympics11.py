import pandas as pd

print("Step 0")
print("========================")
df = pd.read_csv("athlete_events.csv")
print("There are " + str(len(df)) + " records in the data-set.")

print("\nStep 1")
print("========================")
df["Medal"] = df["Medal"].fillna("None")
print("There are " + str(len(df[df["Medal"] != "None"])) + " records in the data-set with medals.")


print("\nStep 2")
print("========================")
g = df.groupby("Sport")["Height"].mean()
print("Tallest:")
print(g.nlargest(3))
print("\nShortest:")
print(g.nsmallest(3))

g = df.groupby("Sport")["Weight"].mean()
print("\nHeaviest:")
print(g.nlargest(3))
print("\nLightest:")
print(g.nsmallest(3))

print("\nStep 3")
print("========================")
f = df[df["Season"] == "Winter"]
years = f.groupby(["Year"]).count().reset_index()["Year"].tolist()
for year in years:
    gg = f[(f["Year"] == year) & (f["Medal"] == "Gold")].groupby("Team")["Medal"].count().nlargest(1).reset_index()
    print(str(year) + " " + gg["Team"][0])
    
print("\nStep 4")
print("========================")
sports = df.groupby("Sport").count().reset_index()["Sport"].tolist()
for sport in sports:
    gg = df[(df["Sport"] == sport) & (df["Medal"] != "None")].groupby("Team").count()["Medal"].nlargest(1).reset_index()
    print(sport + ":: " + gg["Team"][0] + " with " + str(gg["Medal"][0]) + " medals.")
    
print("\nStep 5")
print("========================")
f = df[df["Season"] == "Summer"]
years = f.groupby(["Year"]).count().reset_index()["Year"].tolist()
dataYears = []
dataRates = []
for year in years:
    g = f[f["Year"] == year]
    dataYears.append(year)
    dataRates.append(len(g[g["Sex"] == "F"]) / len(g))

import matplotlib.pyplot as plt
plt.plot(dataYears,dataRates)
plt.show()


print("\nStep 6")
print("========================")
years = df.groupby(["Year"]).count().reset_index()["Year"].tolist()
dataYears = []
dataAges= []
for year in years:
    g = f[f["Year"] == year]
    dataYears.append(year)
    dataAges.append(g["Age"].mean())

import matplotlib.pyplot as plt
plt.plot(dataYears,dataAges)
plt.show()

print("\nStep 7")
print("========================")
f = df[df["Year"] == 2016]
compete_rates = []
for sport in sports:
    ff = f[f["Sport"] == sport]
    if (len(ff) == 0): # perhaps this sport does not exist in this year
        continue
    rate = len(ff[ff["Medal"] != "None"]) / len(ff)
    compete_rates.append({"sport":sport, "rate":rate})

compete_rates = sorted(compete_rates, key = lambda x : x["rate"], reverse=True)
print("We recommend: ")
print(compete_rates[0]["sport"])
print(compete_rates[1]["sport"])
print(compete_rates[2]["sport"])



















