import pandas as pd

df = pd.read_csv("smokers.csv")

df = df[["Year", "State", "Value"]]

print("Step 1")
print("======")
print("# of Surveys: ", len(df))

states = df.groupby(["State"]).count().reset_index()["State"].tolist() #make a list of States
numsurv = df.groupby("State")["Value"].count().reset_index()["Value"].tolist() #make a list of # of survey per state
avgsurv = (sum(numsurv)/len(numsurv))

print("\n")
print("Step 2")
print("======")
print("# of States: ", len(states)) #using list of states
print("Average # of Surveys per State: ", avgsurv)

#step 3
aa = df.sort_values(by=['Value']) #sort the df with 'value' column     
print("\n")
print("Step 3")
print("======")
print("Minimum Recorded Cigarette Use: ")
print(aa.head(1))
print("\n")
print("Maximum Recorded Cigarette Use: ")
print(aa.tail(1))

#step 4
bb = df.groupby("State")["Value"].mean() #group by 'state' column and compute mean of 'value' column
print("\n")
print("Step 4")
print("======")
print("Least Cigarette Use State: ")
print(bb.nsmallest(1))
print("\n")
print("Most Cigarette Use State: ")
print(bb.nlargest(1))

#step 5
cc = df.groupby("State")["Year","Value"].mean() #group by 'state column and compute mean of 'year' and 'value' comlumn
cc = cc.sort_values(by=['Value'], ascending = False)
print("\n")
print("Step 5")
print("======")
print("Top 10 Most Cigarette Use States: ")
print(cc.head(10))

#step 6
print("\n")
print("Step 6")
print("======")
userstate = input("State: ")
useryear = input("Enter Year: ")

dff = df[(df["State"] == userstate) & (df["Year"] == int(useryear))] #filtering data

print("Found ", len(dff), "surveys: ")
print(dff)

#step 7
print("\n")
print("Step 7")
print("======")

while True:
    
    stateinput = input("Enter State: ")
    
    if stateinput == "Exit":
        print("Bye Bye!")
        break
    
    elif stateinput not in states: #use list of states I created at the beginning
        print("hmmm... cannot find that state.")
        print("Compute for another state or enter 'Exit' to exit.")
    
    else:
        dfa = df[df["State"] == stateinput]
        values = dfa.groupby("Year")["Value"].mean().reset_index()["Value"].tolist()
        years = dfa.groupby(["Year"]).count().reset_index()["Year"].tolist()
        
        import matplotlib.pyplot as plt
        plt.plot(years, values)
        plt.show()
        
        if values[len(values)-1] < values[len(values)-2]:
            print("Cigarette use is on decline in ", stateinput)
            print("Compute for another state or enter 'Exit' to exit")
        else:
            print("Cigarette use is on increse ", stateinput)
            print("Compute for another state or enter 'Exit' to exit")
