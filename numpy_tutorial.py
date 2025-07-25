#import numpy
import numpy as np
a=np.array([1,2,3], dtype='int16')
print(a)
b=np.array([[4,5,6],[7,8,9]])
print(b)

#get dimension
dim=a.ndim
print(dim)

#get shape
sh=b.shape
print(sh)

#get datatype
dt=a.dtype
print(dt)

#get size
sz=a.itemsize
print(sz)

#get total size
ts=a.nbytes
print(ts)