#accessing/changing specific elements rows column etc
import numpy as np
a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

#get specific element
print(a[1,5])

#get a specific row
print(a[0,:])

#get specific column
print(a[:,3])

#get a little fancy (begin:end: stepsize)
print(a[0,1:6:2])

#change element
a[1,6]=20
print(a)

#change full column
a[:,3]=5
print(a)

#change full row
a[0,:]=9
print(a)

