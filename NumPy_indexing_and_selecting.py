#NumPy indexing
import numpy as np 
arr= np.arange(0,11)

#easist way to pick an element just like lists
print(arr[8])
print(arr[1:5]) #remeber last element wont be in so from 1 to 5

#numpy broadcasting (a more efficient way)
arr[0:5] = 100 #to change the first 5 values to 100
print(arr)
arr = np.arange(0,11)
teil_arr = arr [0:6] #0 to 5
print(teil_arr)
teil_arr[:] = 99 #to change all teh values of the array
print(teil_arr)
print(arr) #we realize that the values in the orginal array are also changed so the tells us that numpy didnt actully copy the array but instead used it 

#coping an array to stop that :
arr_copy = arr.copy() #to make a copy of our array
print(arr_copy)  #this is a copy array on which operations could be done without changing the orginal array



#now to use that on Matrices
arr_2D = np.array(([5,10,15],[20,25,30],[35,40,45]))
print(arr_2D)
#indexing 
print(arr_2D[1]) #would give the 2nd line of the matrix
print(arr_2D[1][0]) #getting the first element of the 2nd line
print(arr_2D[1,0]) #or it could be written like that 
print(arr_2D[:2]) #getting the first and the 2nd line
print(arr_2D[:2,1:]) #getting all the values starting from the 2nd one and thats from the first and second line so like getting a sub-Matrix

#NumPy selection
arr = np.arange(1,11)
bool_arr = arr > 5
print(bool_arr) #to get the boolean values sotosay True when the Element in arr > 5 
print(arr[bool_arr]) #to get the eliments that has the True values
print(arr[arr<5]) #or it could be wrritten like that

#how its usually used
x=2
print(arr[arr<x])

#using it in Matrices
arr_2d = np.arange(50).reshape(5,10)
print(arr_2d)
print(arr_2d[1:3 , 3:5])
