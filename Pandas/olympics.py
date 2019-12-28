import pandas as pd

df = pd.read_csv("athlete_events.csv")

df["Medal"] = df["Medal"].fillna("None")

dc = df[(df["Medal"] != "None") & (df["Team"] == "South Korea") & (df["Sport"]=="Figure Skating")]
print(dc[["Name", "Year", "Medal"]])