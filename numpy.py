#NumPy (für Linear Algebra) (extremly fast)
import numpy as np
meine_liste=[1,2,3]
#to turn the list into a numpy array
print(np.array(meine_liste))

matrix = [[1,2,3],[4,5,6]]
print(np.array(matrix))

#numpy arrange
print(np.arange(1,10)) #same as the range() func but this one would create a numpy array derictly (from 1 to 9)
print(np.arange(1,11,2)) #just like with range the last num is referring to step

#auto generaiting Matrices:
#numpy zeros
print(np.zeros(3))
print(np.zeros((5,5))) #to make a matrix of zeros 5x5
#same goes for ones
print(np.ones(5))
print(np.ones((3,3))) #3x3 Matrix of ones
#creating an I matrix
print(np.eye(5)) # since its sequared 5 means 5x5

#geting linear array of equal distributed Values
print(np.linspace(0,10,3))  #from 0 to 10 we want 3 values that has equal distributions (which are 0,5,10) v
print(np.linspace(0,10)) #p.s: without writing the number of needed values we would get 50 values 

#random of numpy
print(np.random.rand(2)) #would give us 2 random numbers with equal distributions (between 1 and 0)
print(np.random.rand(2,2)) #to get a matrix 2x2
print(np.random.randint(1,1000,9)) #this would give us an array of 9 random integers between 1 and 1000

#Matrix from arrays
arr= np.arange(25)
ranarr=np.random.randint(0,50,10)
print(arr.reshape(5,5)) #this will turn arr into 5x5 matrix p.s: the reshape numbers should be exactly how many elements are in the array meaining we cant use here for exp (arr.shape(6,6)) else we would get an error1

#getting a number from an array
print(ranarr.max()) #will get the maximum
print(ranarr.argmax()) #will get the pos(indx) of the max number
print(ranarr.min())#getting the min
print(ranarr.argmin())

#getting the shame
print(arr.shape) #shape is an attribute so no need for brackets ()
print(ranarr.shape)
