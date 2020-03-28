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



def rotate3D(x, y, z, alpha, beta, gamma, order = ['x','y','z']):
    
    
    alpha = np.deg2rad(alpha)
    beta = np.deg2rad(beta)
    gamma = np.deg2rad(gamma)
    
    
    Rx = np.array([[1, 0, 0],
                  [0, np.cos(alpha), -np.sin(alpha)],
                  [0, np.sin(alpha), np.cos(alpha)]])
    
    Ry = np.array([[np.cos(beta), 0, np.sin(beta)],
                  [ 0, 1, 0],
                  [-np.sin(beta), 0, np.cos(beta)]])
    
    Rz = np.array([[np.cos(gamma), -np.sin(gamma), 0],
                  [np.sin(gamma), np.cos(gamma), 0],
                  [0, 0, 1]])
    
    Rxyz = np.array([[np.cos(alpha)*np.cos(beta), np.cos(alpha)*np.sin(beta)*np.sin(gamma) - np.sin(alpha)*np.cos(gamma), np.cos(alpha)* np.sin(beta)*np.cos(gamma) + np.sin(alpha)*np.sin(gamma)],
                     [np.sin(alpha)*np.cos(beta), np.sin(alpha)*np.sin(beta)*np.sin(gamma) + np.cos(alpha)*np.cos(gamma), np.sin(alpha)*np.sin(beta)*np.cos(gamma - np.cos(alpha)*np.sin(gamma))],
                     [-np.sin(beta), np.cos(beta)*np.sin(gamma), np.cos(beta)*np.cos(gamma)]])
    R = {'x': Rx, 'y':Ry, 'z': Rz}
    
        

    newX, newY, newZ = [],[],[]
    #newX2, newY2, newZ2 = [],[],[]
    for r in range(x.shape[0]):
        for c in range(x.shape[1]):
            
            tempx, tempy, tempz = x[r,c],y[r,c],z[r,c]
            
            
            for o in range(len(order)):
                
                if order[o] == 'x':
                    tempx, tempy, tempz = R[order[o]] @ np.array([tempx, tempy, tempz])
                    
                if order[o] == 'y':
                    tempx, tempy, tempz = R[order[o]] @ np.array([tempx, tempy, tempz])
                    
                if order[o] == 'z':
                    tempx, tempy, tempz = R[order[o]] @ np.array([tempx, tempy, tempz])
                    
            
            
            
            
            #tempx2, tempy2, tempz2 = Rxyz @ np.array([x[r,c],y[r,c],z[r,c]])
            
            newX.append(tempx)
            newY.append(tempy)
            newZ.append(tempz)
            
            """newX2.append(tempx2)
            newY2.append(tempy2)
            newZ2.append(tempz2)"""
    
    #return np.array(newX), np.array(newY), np.array(newZ),   np.array(newX2), np.array(newY2), np.array(newZ2)
    return np.array(newX), np.array(newY), np.array(newZ)
            
    
   
    

#newx, newy, newz, newx2, newy2, newz2 = rotate3D(X, Y, Z, 0, 0, 90, ('x','y','z'))
newx, newy, newz = rotate3D(x, y, z, 90, 90, 90, ('x','y','z'))


newx = np.round(newx.reshape(img.shape[0],img.shape[1]), decimals=10)
newy = np.round(newy.reshape(img.shape[0],img.shape[1]), decimals=10)
newz = np.round(newz.reshape(img.shape[0],img.shape[1]), decimals=10)

"""newx2 = np.round(newx2.reshape(36,64), decimals=10)
newy2 = np.round(newy2.reshape(36,64), decimals=10) 
newz2 = np.round(newz2.reshape(36,64), decimals=10)
"""
plt.figure(1)
ax = plt.gca(projection='3d')

"""ax.set_xlim3d(0, 20)
ax.set_ylim3d(-20, 20)
ax.set_zlim3d(-20, 20)"""
ax.plot_surface(newx, newy, newz, rstride=1, cstride=1, facecolors=img)

"""plt.figure(2)
ax = plt.gca(projection='3d')
ax.plot_surface(newx2, newy2, newz2, rstride=2, cstride=2, facecolors=img)"""
plt.show()





# [ 2.74911638  4.77180932  1.91629719]
