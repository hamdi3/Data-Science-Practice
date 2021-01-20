#Panda Data Frames
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101) #Defining a seed for the random func

df = pd.DataFrame(randn(5,4),index="A B C D E".split(),columns ="W X Y Z".split()) #the randn would create a 5x4 Matrix with random values and index just like in Series but written with splits for easier handeling, Labels are for rows and columns are to lable columns
print(df)

#Dataframe operations
df["neu"] = df["W"] + df["Y"] #not only can you just make new columns in the dataframes, you could also add the existing frames to each other
print(df)
df.drop("neu",axis=1) #to show/use the data frame without a specific lable "axis=1" for colomns and "axis=0" for rows, this does not delete a thing
df.drop("neu",axis=1,inplace=True) #only by defining inplace as True can we delete something


#selecting from a dataframe
print(df["W"]) #to get the column W, btw this keeps the index
print(df[["W","Z"]]) #to get more than one colomns
print(df.W) #or it could be used like this 
print(df.loc["A"])#to get a row
print(df.iloc[2])#this will get the row "C" since it has the indx 2 in the row list
print(df.loc["B","Y"]) #to get the value of the row B from the y columns
print(df.loc[["A","B"],["W","Y"]]) #to get a subset
print(df>0) #this would print a dataframe with the boolean value of True where the number is > 0 
print(df[df>0]) #to print a dataframe of the dataframe where the value is True if the number > 0 (NaN would be given if the cell is <0)
print(df["W"]>0) #this would only print the boolean values of the "W" Column 
print(df[df["W"]>0]) #meanwhile this would print the entre data frame except the lines where in "W" a number is negativ (Here C would be ignored)
print(df[df["W"]>0][["Y"]]) #get the Column "Y" where the "W" has postiv values
print(df[df["W"]>0][["Y","X","Z"]]) #you can also get more than one column at a time
print(df[(df["W"]>0) & (df["Y"]>1)]) #to add more conditions one need to use "&" instead of "and" since "and" doesnt work with a Dataframe of value like the one we have here
print(df[(df["W"]>0) | (df["Y"]>1)]) #using the or condition

#Datframe index Operations
new = "NY LA LV LN DC".split()
df["Cities"] = new #to add a new column
print(df)
df.set_index("Cities",inplace=True) #to turn Cities into the index
print(df)

#Multi indexing
outter = ["G1","G1","G1","G2","G2","G2"]#by repeating G1 for example we defined that the first 3 sub_indexs are in G1
inner = [1,2,3,1,2,3]
hier_indx = list(zip(outter,inner)) #to combine the two lists
hier_indx = pd.MultiIndex.from_tuples(hier_indx) #defining the Multiindex
df = pd.DataFrame(np.random.randn(6,2),index=hier_indx,columns="A B".split())
print(df)
df.index.names = ["Groups" , "Numbers"] #giving names to index columns
print(df)
#Selecting from Multi indexing
print(df.loc["G1"].loc[2]) #we'd get 2 Values here since the "2" is an inner index used twice
print(df.xs(["G1",1])) #xs is for getting the cross section
print(df.xs(1,level="Numbers"))
