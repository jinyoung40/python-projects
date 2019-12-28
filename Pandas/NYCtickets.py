import pandas as pd
df = pd.read_csv("nyc_parking_tickets.csv")

print("Step 1: Reading file...")
print(len(df), "records were read from file.")

df = df[(df.Registration_State != "99") & (df.Plate_Type != "999") & (df.Vehicle_Make != "") & (df.Vehicle_Year != 0) & (df.Issuer_Code != 0) & (df.Vehicle_Year < 2018)]
print("\n")
print("Step 2: cleaning file...")
print(len(df), "records after cleanup.")

years = df.groupby(["Vehicle_Year"]).count().reset_index()["Vehicle_Year"].tolist()
tickets = []

for year in years:
    ddf = df[df["Vehicle_Year"] == year]
    ticket = ddf["Vehicle_Year"].count()
    tickets.append(ticket)
import matplotlib.pyplot as plt
plt.plot(years, tickets)
plt.show()

aa = df.groupby("Vehicle_Make").count()
ab = aa.nlargest(5, "Plate_ID")
print("\n")
print("Top 5 vehicle-makes with most tickets...")
print(ab.Plate_ID)

ac = df[df.Plate_Type == "COM"]
stac = ac.groupby("Street_Name").count()
stacd = stac.nlargest(1, "Plate_ID")
print("\n")
print("The street where commercial vehicles got the most tickets:")
print(stacd.Plate_ID)

ad = df.groupby("Registration_State").mean()
add = ad.sort_values(by=["Vehicle_Year"], ascending=False)
add = add["Vehicle_Year"]
print("\n")
print("The state with newest vehicles:")
print(add.head(1))
print("\n")
print("The state with oldest vehicles:")
print(add.tail(1))