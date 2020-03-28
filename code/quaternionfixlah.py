import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2


image = cv2.imread('azunyanKecil.jpg')
img = image[...,::-1].copy()
print(img.shape)
img = img / img.max()
img = np.dstack((img, np.ones(img.shape[:2])))

x, y = np.mgrid[0:img.shape[0], 0:img.shape[1]]
print (x.shape)

# A blank, straight 0 Z coordinate
z = np.zeros(x.shape)
xyzZip = zip (x, y, z)



def getQuaternion(vector, angle = 0):
    
    w = np.cos(angle/2)
    x = vector[0]*np.sin(angle/2)
    y = vector[1]*np.sin(angle/2)
    z = vector[2]*np.sin(angle/2)
    
    return np.array([w, x, y, z])
   
def quaInverse(vector):
    return np.array([vector[0], -vector[1], -vector[2], -vector[3]])

def quaMultiQua(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2

    return np.array([w,x,y,z])

def quaMultiVec(q1, v):
    quaInv = quaInverse(q1)
    return quaMultiQua(quaMultiQua(q1, v), quaInv)[1:]
    
def multiplyList(lst):
    result = 1
    for x in lst:
        result *= x
    return result    
    
def transform(x, y, z, axisRotation, angle):
    angle = np.deg2rad(angle) #quaternion akan membagi angle dengan 2
    
    axis = [[axisRotation[0], 0, 0],
            [0, axisRotation[1], 0],
            [0, 0, axisRotation[2]]]
    axis.reverse()
    
    print (axis)
    row, col = x.shape
    
    
    newX, newY, newZ = [],[],[]
    for r in range(row):
        for c in range(col):
            
            for xx in range(3):
                if xx == 0:
                    qua = getQuaternion(axis[xx], angle)
                else:
                    qua = quaMultiQua(qua, getQuaternion(axis[xx], angle))
            
                    
            tempx, tempy, tempz = quaMultiVec(qua, [0, r, c, z[r,c]]) 
            
           
            newX.append(tempx)
            newY.append(tempy)
            newZ.append(tempz)
            
    return np.array(newX), np.array(newY), np.array(newZ)



axisOfRotation = [1, 1, 0] # [x, y, z] bisa jadi koma, kalu jadi koma angle dikali koma ... x, y, z bisa di isi bersamaan


#newx, newy, newz, newx2, newy2, newz2 = rotate3D(X, Y, Z, 0, 0, 90, ('x','y','z'))
newx, newy, newz = transform(x, y, z, axisOfRotation, 90)


newx = np.round(newx.reshape(img.shape[0],img.shape[1]), decimals=10)
newy = np.round(newy.reshape(img.shape[0],img.shape[1]), decimals=10)
newz = np.round(newz.reshape(img.shape[0],img.shape[1]), decimals=10)

"""newx2 = np.round(newx2.reshape(36,64), decimals=10)
newy2 = np.round(newy2.reshape(36,64), decimals=10) 
newz2 = np.round(newz2.reshape(36,64), decimals=10)
"""
plt.figure(1)
ax = plt.gca(projection='3d')

"""ax.set_xlim3d(-100, 100)
ax.set_ylim3d(-100, 100)
ax.set_zlim3d(-100, 100)"""
ax.plot_surface(newx, newy, newz, rstride=1, cstride=1, facecolors=img)

"""plt.figure(2)
ax = plt.gca(projection='3d')
ax.plot_surface(newx2, newy2, newz2, rstride=2, cstride=2, facecolors=img)"""
plt.show()





# [ 2.74911638  4.77180932  1.91629719]