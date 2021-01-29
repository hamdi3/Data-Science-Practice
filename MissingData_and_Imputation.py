#Missing Data und Imputation
import numpy as np
import pandas as pd 

df = pd.DataFrame({"A": [1,2,np.nan], "B": [5,np.nan,np.nan],"C" : [1,2,3] })#np.nan is basicly for no-value
print(df)

#Elimination Method where Missing data would just be droped -> can cause a problem
df.dropna() #to drop all the rows where there's a NaN leaving only one row (the first row). -> this leads to Missing Data. 
df.dropna(axis=1) #standard value of axis is 0 which is for rows and 1 for coloumns so this drops all coloumns with NaN
print(df) # remember it wont change withould "inplace=True"
df.dropna(thresh=2)#droping all the rows with min. 2 NaN
df.fillna(value="Füllwert")#to replace the NaN cells with a specific value. 
df.fillna(value=0) #can be filled with any type of value
df["A"].fillna(value=df["A"].mean())#you can pick a specific colomn to replace its NaN,
#(the df["A"].mean() means that the cells will be filled with the mean value of "A") (mean = (1+2)/2=1.5)
df["A"].fillna(value=df["A"].sum()) #to fill with the sum of "A"
