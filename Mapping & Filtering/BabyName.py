#Creating class and fields
class Baby:
    Year = 0
    Name = ""
    Percent = 0.0
    Sex = ""
    
    def __init__(self,year,name,percent,sex): #Creating constructor
        self.Year = year
        self.Name = name
        self.Percent = percent
        self.Sex = sex

#importing data from csv file downloaded
f = open("baby-names.csv") 
import csv
reader = csv.reader(f)
next(reader)

babies = []

for row in reader:
    b = Baby(int(row[0]), row[1], float(row[2]), row[3])
    babies.append(b)

#Step 1: finding most peak given name
print("Step 1: Most Peak Given Name")
print("============================")

#using max function to find most peak given name
mostname = max(babies, key = lambda x:x.Percent)

print("Name ", mostname.Name, "was given to ", mostname.Percent*100, "% of babies in ", mostname.Year)

#Step 2: Recommendation Method 1
print("\n")
print("Step 2: Recommendation Method 1")
print("===============================")

#creating user input
gender = input("Gender (girl/boy): ")
style = input("Style (modern/classic/none): ")

#filtering and mapping data
if style == "modern":
    modernfiltered = list(filter(lambda x:x.Sex == gender and x.Year >= 1900, babies))
    modernmax = max(modernfiltered, key=lambda x: x.Percent)
    print("We suggest the name ", modernmax.Name)
elif style == "classic":
    classicfiltered = list(filter(lambda x:x.Sex == gender and x.Year <= 1899, babies))
    classicmax = max(classicfiltered, key = lambda x:x.Percent)
    print("We suggest the name ", classicmax.Name)
elif style =="none":
    filtered = list(filter(lambda x:x.Sex == gender, babies))
    anymax = max(filtered, key = lambda x:x.Percent)
    print("We suggest the name ", anymax.Name)

#Step 3 : Recommendation Method 2
print("\n")
print("Step 3: Recommendation Method 2")
print("===============================")

name = input("Name: ")

namefiltered = list(filter(lambda x:x.Name==name, babies)) #filtering with name
filteredyear = max(namefiltered, key=lambda x:x.Percent)  #year inputed name was most popular
targetyear = list(filter(lambda y: y.Year == filteredyear.Year and y.Sex == filteredyear.Sex, babies)) #filtering with year and sex
mostnametarget = max(targetyear, key=lambda y: y.Percent) 

print(filteredyear.Name, "was most popular in ", filteredyear.Year)

if mostnametarget.Name != name: 
    print("We suggest the name ", mostnametarget.Name) #only when most popular name is not same with input name
else:
    targetyear.remove(mostnametarget) #when input name is the most popular name, suggesting second most popular name
    secondnametarget = max(targetyear, key=lambda y:y.Percent)
    print("We suggest the name ", secondnametarget.Name)

#step 4: Populartity Graph
print("\n")
print("Step 4: Popularity Graph")
print("===============================")

nametwo = input("Name: ")
gendertwo = input("Gender (girl/boy): ")

graphdata =[]

#create label for x axis
labels = []

namegenderdata = list(filter(lambda x:x.Name == nametwo and x.Sex == gendertwo, babies)) 
xplotdata = list(map(lambda x:x.Percent, namegenderdata))
yplotdata = list(map(lambda x:x.Year, namegenderdata))

#appending values to graph data
for x in range (len(namegenderdata)):
    graphdata.append(xplotdata[x])
    labels.append(yplotdata[x])
    
import matplotlib.pylab as plt
plt.plot(labels, graphdata)

plt.show()


