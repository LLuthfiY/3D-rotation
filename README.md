# 3D-rotation

Muhammad Luthfi A
1313617033
## ROTATION 3D
euler rotation 

![ori](https://github.com/LLuthfiY/3D-rotation/blob/master/img/ori.jpg)
### ori

![x90](https://github.com/LLuthfiY/3D-rotation/blob/master/img/x90.jpg)
### x90

![y90](https://github.com/LLuthfiY/3D-rotation/blob/master/img/y90.jpg)
### y90

![z90](https://github.com/LLuthfiY/3D-rotation/blob/master/img/z90.jpg)
### z90

## euler

dengan mengkalikan dot product untuk setiap coordinate dengan euler angle matrix, kita dapat mendapatkan coordinate aru hasil rotasi

```
[[1,             0,              0],
 [0, np.cos(alpha), -np.sin(alpha)],
 [0, np.sin(alpha),  np.cos(alpha)]]
```
untuk merotasi terhadap X


```
[[ np.cos(beta), 0, np.sin(beta)],
 [            0, 1,            0],
 [-np.sin(beta), 0, np.cos(beta)]]
```
untuk merotasi terhadap Y


```
[[np.cos(gamma), -np.sin(gamma), 0],
 [np.sin(gamma),  np.cos(gamma), 0],
 [            0,          0,     1]]
```
untuk merotasi terhadap Z


```
Matrix @ [x, y, z]
```

## Axis
literally rotasi 2D dijadikan rotasi 3D
dengan menggunakan matrix rotasi 2D
```
[[np.cos(angle), -np.sin(angle), 0],
 [np.sin(angle),  np.cos(angle), 0],
 [            0,          0,     1]]
```
yang dikalikan dot product dengan koordinat yang sesuai terhadap rotasinya
```
[Y, Z, 1] untuk rotasi terhadap X axis
[X, Z, 1] untuk rotasi terhadap Y axis
[X, Y, 1] untuk rotasi terhadap z axis
```
akan menghasilkan sebuah koordinat baru hasil dari rotasi 

## convert to code

## euler
```
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
    R = {'x': Rx, 'y':Ry, 'z': Rz}
```
setiap rotasi dipisah agar masing masing dapat di*dot product*kan menjadi matrix 
![eulerMatrix](https://github.com/LLuthfiY/3D-rotation/blob/master/img/unnecessary/Untitled.jpg)


```
    newX, newY, newZ = [],[],[]
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
    
    
    return np.array(newX), np.array(newY), np.array(newZ)
```
mangkali*dot product*kan koordinat dan matrix sesuai dengan urutan 


## Axis
sama
```
def rotate3D(x, y, z, alpha, beta, gamma, order = ['x','y','z']):
    
    
    alpha = np.deg2rad(alpha)
    beta = np.deg2rad(beta)
    gamma = np.deg2rad(gamma)
    
    Rz = np.array([[np.cos(gamma), -np.sin(gamma), 0],
                  [np.sin(gamma), np.cos(gamma), 0],
                  [0, 0, 1]])
    
    
        

    newX, newY, newZ = [],[],[]
    #newX2, newY2, newZ2 = [],[],[]
    for r in range(x.shape[0]):
        for c in range(x.shape[1]):
            
            tempx, tempy, tempz = x[r,c],y[r,c],z[r,c]
            
            
            for o in range(len(order)):
                
                if order[o] == 'x':
                    Rz = getMatrix(alpha)
                    tempy, tempz, scale = Rz @ np.array([tempy, tempz, 1]).T
                    tempy, tempz = tempy/scale, tempz/scale
                if order[o] == 'y':
                    Rz = getMatrix(beta)
                    tempx, tempz, scale = Rz @ np.array([tempx, tempz, 1]).T
                    tempx, tempz = tempx/scale, tempz/scale
                if order[o] == 'z':
                    Rz = getMatrix(gamma)
                    tempx, tempy, scale = Rz @ np.array([tempx, tempy, 1]).T
                    tempx, tempy = tempx/scale, tempy/scale
            
            
            
            
            #tempx2, tempy2, tempz2 = Rxyz @ np.array([x[r,c],y[r,c],z[r,c]])
            
            newX.append(tempx)
            newY.append(tempy)
            newZ.append(tempz)
            
            """newX2.append(tempx2)
            newY2.append(tempy2)
            newZ2.append(tempz2)"""
    
    #return np.array(newX), np.array(newY), np.array(newZ),   np.array(newX2), np.array(newY2), np.array(newZ2)
    return np.array(newX), np.array(newY), np.array(newZ)
```

```
def getMatrix(angle):
    return np.array([[np.cos(angle), -np.sin(angle), 0],
                     [np.sin(angle), np.cos(angle), 0],
                     [0, 0, 1]])
```
## interesting things
![ori](https://github.com/LLuthfiY/3D-rotation/blob/master/img/Untitled2.jpg)

terdapat sedikit miss calculation untuk x90, z90, y90

jadi hasil dari programnya harus diround terlebih dahulu
![ori](https://github.com/LLuthfiY/3D-rotation/blob/master/img/all90.jpg)

