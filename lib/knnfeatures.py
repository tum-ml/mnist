import numpy as np
import math as math

def mass(image):
    image = np.array(image)
    return np.sum(image)/255

def averagemass(image):
    m = mass(image)
    return m/image.size

def lrmass(image):
    image = np.array(image)
    dim = np.shape(image)
    mid = dim[1]/2
    leftmass = 0
    rightmass = 0
    for j in range(dim[1]):
        if(j<mid):
            leftmass = leftmass + np.sum(image[:,j])
        else:
            rightmass = rightmass + np.sum(image[:,j])
    return (leftmass/255,rightmass/255)

def averagelrmass(image):
    lrm = lrmass(image)
    m = mass(image)
    return (lrm[0]/m,lrm[1]/m)

def tbmass(image): 
    image = np.array(image)
    dim = np.shape(image)
    mid = dim[0]/2
    topmass = 0
    bottommass = 0
    for i in range(dim[0]):
        if(i<mid):
            topmass = topmass + np.sum(image[i,:])
        else:
            bottommass = bottommass + np.sum(image[i,:])
    return (topmass/255,bottommass/255)

def averagetbmass(image):
    tbm = tbmass(image)
    m = mass(image)
    return (tbm[0]/m,tbm[1]/m)

def avgHorizontalStroke(image):
    dim = np.shape(image)
    stroke = 0
    for i in range(dim[0]):
        strokeSize = [0]
        count = 0
        for j in range(dim[1]):
            if(image[i,j]>0):
                count += 1
            else:
                strokeSize.append(count)
                count=0
        stroke = np.amax(np.array(strokeSize))*(i+1)/dim[1]
    return stroke

def avgVerticalStroke(image):
    dim = np.shape(image)
    stroke = 0
    for j in range(dim[1]):
        strokeSize = [0]
        count = 0
        for i in range(dim[0]):
            if(image[i,j]>0):
                count += 1
            else:
                strokeSize.append(count)
                count=0
        stroke = np.amax(np.array(strokeSize))*(j+1)/dim[0]
    return stroke
            
def edgeLength(image):
    dim = np.shape(image)
    
    
def transitions(image):
    dim = np.shape(image)
    t = 0
    for i in range(dim[0]):
        for j in range(dim[1]-1):
            if(image[i,j]!=image[i,j+1]):
                t+=1
    return t
    
def topBoundaryTouch(image,pix=2):
    dim = np.shape(image)
    pix = dim[0]-1 if dim[0]<pix else pix
    b = 0
    for i in range(pix):
        b += (np.sum(image[i,:]))/255
    return b

def bottomBoundaryTouch(image,pix=2):
    dim = np.shape(image)
    pix = dim[0]-1 if dim[0]<pix else pix
    b = 0
    for i in range(pix):
        b += (np.sum(image[dim[0]-i-1,:]))/255
    return b

def leftBoundaryTouch(image,pix=2):
    dim = np.shape(image)
    pix = dim[1]-1 if dim[1]<pix else pix
    b = 0
    for i in range(pix):
        b += (np.sum(image[:,0]))/255
    return b

def rightBoundaryTouch(image,pix=2):
    dim = np.shape(image)
    pix = dim[1]-1 if dim[1]<pix else pix
    b = 0
    for i in range(pix):
        b += (np.sum(image[:,dim[1]-1-i]))/255
    return b

def aspectRatio(image):
    dim = np.shape(image)
    return dim[0]/dim[1]

def avgDistanceFromImageCenter(image):
    dim = np.shape(image)
    m = mass(image)
    center = np.array([int(dim[0]/2),int(dim[1]/2)])
    distance = 0
    for i in range(dim[0]):
        for j in range(dim[1]):
            if(image[i,j]>0):
                point = np.array([i,j])
                dis = sum(pow(center-point,2))
                distance += math.sqrt(dis)
    return distance/m
    
def lrRatio(image):
    l,r = lrmass(image)
    ra = 0
    if r!=0:
        ra=l/r
    return ra

def tbRatio(image):
    t,b = tbmass(image)
    r=0
    if b!=0:
        r=t/b
    return r

def ySymmetric(image):
    dim = np.shape(image)
    count = 0
    for i in range(dim[0]):
        for j in range(int(dim[1]/2)):
            if(image[i,j]==image[i,dim[1]-j-1]):
                count+=1
    m = mass(image)
    return count/m

def xSymmetric(image):
    dim = np.shape(image)
    count = 0
    for j in range(dim[1]):
        for i in range(int(dim[0]/2)):
            if(image[i,j]==image[dim[0]-i-1,j]):
                count+=1
    m = mass(image)
    return count/m

def ySymmetric2(image):
    dim = np.shape(image)
    count = 0
    for i in range(dim[0]):
        for j in range(int(dim[1]/2)):
            if(image[i,j]==image[dim[0]-i-1,dim[1]-j-1]):
                count+=1
    m = mass(image)
    return count/m
                
            