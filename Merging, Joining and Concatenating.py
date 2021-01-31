#Merging, Joining and Concatenating
import pandas as pd

df1 = pd.DataFrame({"A" : ["A0","A1","A2","A3"],
                    "B" : ["B0","B1","B2","B3"],
                    "C" : ["C0","C1","C2","C3"],
                    "D" : ["D0","D1","D2","D3"]},
                    index=[0, 1, 2, 3])
df2 = pd.DataFrame({"A" : ["A4","A5","A6","A7"],
                    "B" : ["B4","B5","B6","B7"],
                    "C" : ["C4","C5","C6","C7"],
                    "D" : ["D4","D5","D6","D7"]},
                    index=[4, 5, 6, 7])
df3 = pd.DataFrame({"A" : ["A8","A9","A10","A11"],
                    "B" : ["B8","B9","B10","B11"],
                    "C" : ["C8","C9","C10","C11"],
                    "D" : ["D8","D9","D10","D11"]},
                    index=[8, 9, 10, 11])
pd.concat([df1,df2,df3],axis=0) #the axis=0 so that no extra Colomns would be made.
pd.concat([df1,df2,df3],axis=1)


links = pd.DataFrame({"key": ["K0","K1","K2","K3"],
                        "A": ["A0","A1","A2","A3"],
                        "B": ["B0","B1","B2","B3"]})
rechts = pd.DataFrame({"key": ["K0","K1","K2","K3"],
                        "A": ["C0","C1","C2","C3"],
                        "B": ["D0","D1","D2","D3"]})
print(pd.merge(links,rechts,how="inner",on="key")) #here we combain the 2 of them using key as a combaining coluomn and using inner as a joining type

links = pd.DataFrame({"key1": ["K0","K0","K1","K2"],
                      "key2": ["K0","K1","K0","K1"],
                        "A": ["A0","A1","A2","A3"],
                        "B": ["B0","B1","B2","B3"]})
rechts = pd.DataFrame({"key1": ["K0","K1","K1","K2"],
                       "key2": ["K0","K0","K0","K0"],
                        "A": ["C0","C1","C2","C3"],
                        "B": ["D0","D1","D2","D3"]})
pd.merge(links,rechts,how ="right", on=["key1","key2"]) #using the recht dataframe as a basis for merging -> no NaN value by rechts
pd.merge(links,rechts,how ="left", on=["key1","key2"]) #using the links dataframe as a basis for merging -> no NaN values by links
