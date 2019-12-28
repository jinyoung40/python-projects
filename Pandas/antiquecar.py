import pandas as pd

df = pd.read_csv("cars.csv")
df = df[["Model", "MPG", "Horsepower", "Origin"]]

while True:
    print("Welcome to Antique Car Search")
    print("=============================")
    print("1 - Search Car")
    print("2 - Green Best/Worst Report")
    print("3 - Car Origin Report")
    print("0 - Exit")
    user = int(input(" What do you want to do? "))
    
    if user == 0:
        break
    elif user == 1:
        #feature #1
        mnmpg = input("Required Min. MPG: ")
        mnhorse = input("Required Min. Horsepower: ")

        aa = df[(df["MPG"] >= int(mnmpg)) & (df["Horsepower"]>= int(mnhorse))]
        print("\n")
        print("Found ", len(aa), "cars matching the criteria.")
        print(aa["Model"])
        print("\n")

    elif user == 2:
        #feature #2
        avg = df["MPG"].mean()
        print("\n")
        print("Avg. MPG of all cars is: ", avg)
        grn = df.iloc[df["MPG"].idxmax()]
        print("Greenest car is ", grn["Model"], " with ", grn["MPG"], "MPG.")
        wst = df.iloc[df["MPG"].idxmin()]
        print("Worst car is ", wst["Model"], " with ", wst["MPG"], "MPG.")
        print("\n")

    elif user == 3:
        #feature #3
        print("\n")
        bb = df.groupby("Origin").count()
        print("There are cars from ", len(bb), "origins.")
        print(bb["Model"])
        print("\n")