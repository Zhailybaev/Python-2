from pandas import *
import matplotlib.pyplot as plt

df=read_csv('C:\\Users\\Asus\\Desktop\\ghjuf\\python2\\hw\\hw 8\\WORLD UNIVERSITY RANKINGS.csv')

newdf1 = df.mask((df['Employability Rank']) == "-", 0)
newdf1['Employability Rank']=newdf1['Employability Rank'].astype(float)
df1=newdf1.nlargest(10,"Employability Rank")  #1 function for 10 smallest university's rank
#print(df1)

newdf2 = df.mask((df['Employability Rank']) == "-", 20000)
newdf2['Employability Rank']=newdf2['Employability Rank'].astype(float)
df2=newdf2.nsmallest(10,"Employability Rank") #2 function for 10 largest university's rank
#print(df2)

#print(df.loc[lambda df: df['Location']=="United Kingdom"]) #3 function for printing UK universities 

#print(df["Score"].mean()) #4 function that returns the average value of Score

#print(df.query("Research Rank == Education Rank"))

#print(df[df["Research Rank"] == df["Employability Rank"]]) #5 function where Research Rank=Employability Rank
#print(df)


newdf3=df.mask((df['World Rank']) > 100)
newdf4=newdf3.dropna()

newdf5=newdf4['Location'].value_counts().to_frame()
newdf5 = newdf5.reset_index()
newdf5.columns = ['Location', 'number']

plt.pie(newdf5["number"],labels=newdf5["Location"]) #Pie Charts where we have top 100 universities with their location
plt.show()
print(newdf5)