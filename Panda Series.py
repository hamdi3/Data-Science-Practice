#Panda Series
import numpy as np
import pandas as pd

#Input-Data
labels = ["a","b","c"]
lst = [10,20,30]
arr = np.array(lst)
dic = {"a":10,"b":20,"c":30}


#Using Pandas on the input-data :

print(pd.Series(data=lst)) #since lst doesnt contain a label byitself pandas would use the index as the labels

print(pd.Series(data=lst,index=labels))#here we used the list lables for indexing the Series that was made from lst

print(pd.Series(lst,labels)) #this does the same as the one before it so we dont need to wirte "data, index =" 

print(pd.Series(arr,labels)) #pandas works with numpy arrays justfine

print(pd.Series(dic)) #since Dics have key on their own, they will be used for labeling 

#The datatypes:

print(pd.Series(data=labels)) # this show us that pandas can also contain strings

print(pd.Series([sum,print,len])) #pandas can contain functions, this isnt used much but its just to show how flexible pandas is. 

Seri = pd.Series([1,2,3,4],index=["USA","Austeria","Germany","Korea"])
Seri2= pd.Series([5,6,7,8],index=["USA","Austeria","Japan","Korea"])
print(Seri["USA"]) #to get the value of the index just like dics

print(Seri + Seri2) # you can add Series to each other just notice that the data only get added if there were data in the other Serie with the same index
                    #if not the index isnt in both itll have a NaN value
