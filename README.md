# 3D-rotation

Muhammad Luthfi A
1313617033
## ROTATION 3D
euler rotation 
### ori
![ori](https://github.com/LLuthfiY/3D-rotation/blob/master/img/ori.jpg)



### x90
![x90](https://github.com/LLuthfiY/3D-rotation/blob/master/img/x90.jpg)



### y90
![y90](https://github.com/LLuthfiY/3D-rotation/blob/master/img/y90.jpg)



### z90
![z90](https://github.com/LLuthfiY/3D-rotation/blob/master/img/z90.jpg)


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
 [            0,              0, 1]]
```
yang dikalikan dot product dengan koordinat yang sesuai terhadap rotasinya
```
[Y, Z, 1] untuk rotasi terhadap X axis
[X, Z, 1] untuk rotasi terhadap Y axis
[X, Y, 1] untuk rotasi terhadap z axis
```
akan menghasilkan sebuah koordinat baru hasil dari rotasi 

## Quaternion
anggap saja kita memiliki fungsi quaternion2D yang gambarnya seperti berikut
![quaternion2D](https://github.com/LLuthfiY/3D-rotation/blob/master/img/quaternionExplain/quater2D.jpg)
##### x = cos(theta), y = sin(theta)


look familiar? NO? how about This?
![quaternion2Dimaginer](https://github.com/LLuthfiY/3D-rotation/blob/master/img/quaternionExplain/quater2DImaginer.jpg)
##### real = cos(theta), i = sin(theta)


dengan gambar diatas kita bisa menebak bentuk dari quaternion
![quaternion4D](https://github.com/LLuthfiY/3D-rotation/blob/master/img/quaternionExplain/4D.jpg)
##### real = cos(theta), i = sin(theta), j = sin(theta), k = sin(theta)


sehingga didapatkan rumus 
> quaternion = (cos(theta), sin(theta), sin(theta), sin(theta))
dan 
> p' = q * p
##### tapi
jika dilakukan hal seperti itu, rotasi nya akan menjadi rotasi 4D

maka dari itu, muncullah IDE utama dari quaternion rotation, yaitu membagi rotasinya menjadi 2 tahap:
- tahap pertama menjalankan rotasi hingga setengah bagian
- tahap kedua melanjutkan rotasi sambil menghilangkan rotasi dimensi ke 4

![rotasi4Dgraph](https://github.com/LLuthfiY/3D-rotation/blob/master/img/quaternionExplain/4Dgraph2.jpg)
##### 
sehingga diperoleh rumus 
> quaternion = (cos(theta/2), sin(theta/2), sin(theta/2), sin(theta/2))
dan 
> p' = q * p * q^-1

# convert to code

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

## Quaternion
main code
```
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
```
quaternion ke xx dikali dengan quaternion selanjutnya agar dapat melakukan rotasi 2 axis / lebih

get Quaternion
```
def getQuaternion(vector, angle = 0):
    
    w = np.cos(angle/2)
    x = vector[0]*np.sin(angle/2)
    y = vector[1]*np.sin(angle/2)
    z = vector[2]*np.sin(angle/2)
    
    return np.array([w, x, y, z])
```
-----------------------------------------------------------------------------------------
inverse Quaternion
```
def quaInverse(vector):
    return np.array([vector[0], -vector[1], -vector[2], -vector[3]])
```
-----------------------------------------------------------------------------------------
Quaternion * Quaternion
```
def quaMultiQua(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2

    return np.array([w,x,y,z])
```
------------------------------------------------------------------------------------------
p' = q * p * q^-1
```
def quaMultiVec(q1, v):
    quaInv = quaInverse(q1)
    return quaMultiQua(quaMultiQua(q1, v), quaInv)[1:]
```
## interesting things
![ori](https://github.com/LLuthfiY/3D-rotation/blob/master/img/Untitled2.jpg)
#### warna biru karena saya meng import gambar dengan open cv
terdapat sedikit miss calculation untuk x90, z90, y90

jadi hasil dari programnya harus diround terlebih dahulu
![ori](https://github.com/LLuthfiY/3D-rotation/blob/master/img/all90.jpg)


# BONUS
![BONUS](https://github.com/LLuthfiY/3D-rotation/blob/master/img/unnecessary/meme.jpg)
