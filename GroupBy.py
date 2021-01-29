#To group data by specific parameters
import pandas as pd 

data = {"Firma" : ["GOOG","GOOG","MSFT","MSFT","FB","FB"],
        "Person": ["Sam","Charlie","Amy","Vanessa","Carl","Sarah"],
        "Sales" : [200,120,340,124,243,350]}
df = pd.DataFrame(data)
df.groupby("Firma").mean() #to get the mean of each Firma
nach_firma = df.groupby("Firma")
nach_firma.mean() # or it could be done like this
nach_firma.std() #to get the standard deviation
nach_firma.min() #to get the min. sale 
nach_firma.max() #the max sale 
nach_firma.count() #to get the count
nach_firma.describe() #this will give a describtion of the dataframe
nach_firma.describe().transpose() #to get the transperent matrix of it
nach_firma.describe().transpose()["GOOG"] #to get a data of a specific row
