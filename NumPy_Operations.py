#NumPy Operations
import numpy as np
arr = np.arange(0,10)
#math-operatioins can be used on arrays for example
print(arr+arr)
print(arr*arr)
print(arr-arr)
print(arr/arr) #[0] would be nan since you cant devide 0 by 0
print(1/arr) #[0] would be inf since 1/0=inf 
print(arr**3)
print(np.sqrt(arr)) #to get the sequare
print(np.exp(arr)) # to get the exponent e^
print(np.max(arr))
print(arr.max())#same as the np one before it
print(arr.min())
print(np.sin(arr))#to get the sin value of each array element
print(np.cos(arr))#for cos value
print(np.log(arr))#to get the logarithm of array eliments
