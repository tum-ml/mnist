import numpy as np
import numpy.ma as ma

def thresholding(image,th=128):
    image = np.array(image)
    image = image>th
    return image*255

def thinning(image,th=3):
    image = np.array(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            sum = np.sum(image[i,j:j+th])
            discontinuity = (image[i-1,j]==0 and image[1+1,j]==0)
            if(sum==th*255 and not discontinuity):
                image[i,j]=0
                j = j+th
    return image

def boundarysquare(image):
    image = np.array(image)
    dim = np.shape(image)
    topRow = leftColumn = 0
    bottomRow = dim[0]
    rightColumn = dim[1]
    topRowFound = bottomRowFound = leftColumnFound = rightColumnFound = False
    
    for i in range(dim[0]):
        s = np.sum(image[i,:])
        if(s>0 and not topRowFound):
            topRow = i
            topRowFound = True
        if(s==0 and topRowFound and not bottomRowFound):
            bottomRow = i
            bottomRowFound = True
        
    for j in range(dim[1]):
        s = np.sum(image[:,j])
        if(s>0 and not leftColumnFound):
            leftColumn = j
            leftColumnFound = True
        if(s==0 and leftColumnFound and not rightColumnFound):
            rightColumn = j
            rightColumnFound = True
    
    return image[topRow:bottomRow,leftColumn:rightColumn]


def thin(image):
    image = np.array(image)
    dim = np.shape(image)
    markedPixels = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            neighbours = []
            img = image[i,j]
            if(i>0 and i<dim[0]-1 and j>0 and j<dim[1]-1):
                neighbours.append(image[i-1,j])
                neighbours.append(image[i-1,j+1])
                neighbours.append(image[i,j+1])
                neighbours.append(image[i+1,j+1])
                neighbours.append(image[i+1,j])
                neighbours.append(image[i+1,j-1])
                neighbours.append(image[i,j-1])
                neighbours.append(image[i-1,j-1])
            elif(i==0 and j>0 and j<dim[1]-1):
                neighbours.append(image[i,j+1])
                neighbours.append(image[i+1,j+1])
                neighbours.append(image[i+1,j])
                neighbours.append(image[i+1,j-1])
                neighbours.append(image[i,j-1])
            elif(i==dim[0]-1 and j>0 and j<dim[1]-1):
                neighbours.append(image[i-1,j])
                neighbours.append(image[i-1,j+1])
                neighbours.append(image[i,j+1])
                neighbours.append(image[i,j-1])
                neighbours.append(image[i-1,j-1])
            elif(i>0 and i<dim[0]-1 and j==0):
                neighbours.append(image[i-1,j])
                neighbours.append(image[i-1,j+1])
                neighbours.append(image[i,j+1])
                neighbours.append(image[i+1,j+1])
                neighbours.append(image[i+1,j])
            elif(i>0 and i<dim[0]-1 and j==dim[1]-1):
                neighbours.append(image[i-1,j])
                neighbours.append(image[i+1,j])
                neighbours.append(image[i+1,j-1])
                neighbours.append(image[i,j-1])
                neighbours.append(image[i-1,j-1])
            elif(i==0 and j==0):
                neighbours.append(image[i,j+1])
                neighbours.append(image[i+1,j+1])
                neighbours.append(image[i+1,j])
            elif(i==0 and j==dim[1]-1):
                neighbours.append(image[i+1,j])
                neighbours.append(image[i+1,j-1])
                neighbours.append(image[i,j-1])
            elif(i==dim[0]-1 and j==0):
                neighbours.append(image[i-1,j])
                neighbours.append(image[i,j+1])
                neighbours.append(image[i-1,j+1])
            elif(i==dim[0]-1 and j==dim[1]-1):
                neighbours.append(image[i-1,j])
                neighbours.append(image[i,j-1])
                neighbours.append(image[i-1,j-1])
            nonZeroNeighboursCount = np.sum(neighbours)/255
            transitionCount = 0
            for k in range(len(neighbours)-1):
                if(neighbours[k]!=neighbours[k+1]):
                    transitionCount+=1
            if(transitionCount<2 or nonZeroNeighboursCount not in [0,1,7,8]):
                #markedPixels.append([i,j])
                image[i,j]=0
    for p in markedPixels:
        image[p[0],p[1]]=0
    return image

def fetchNeighbours(image,i,j):
    neighbours = []
    dim = np.shape(image)
    if(i>0 and i<dim[0]-1 and j>0 and j<dim[1]-1):
        neighbours.append(image[i-1,j])
        neighbours.append(image[i-1,j+1])
        neighbours.append(image[i,j+1])
        neighbours.append(image[i+1,j+1])
        neighbours.append(image[i+1,j])
        neighbours.append(image[i+1,j-1])
        neighbours.append(image[i,j-1])
        neighbours.append(image[i-1,j-1])
    elif(i==0 and j>0 and j<dim[1]-1):
        neighbours.append(image[i,j+1])
        neighbours.append(image[i+1,j+1])
        neighbours.append(image[i+1,j])
        neighbours.append(image[i+1,j-1])
        neighbours.append(image[i,j-1])
    elif(i==dim[0]-1 and j>0 and j<dim[1]-1):
        neighbours.append(image[i-1,j])
        neighbours.append(image[i-1,j+1])
        neighbours.append(image[i,j+1])
        neighbours.append(image[i,j-1])
        neighbours.append(image[i-1,j-1])
    elif(i>0 and i<dim[0]-1 and j==0):
        neighbours.append(image[i-1,j])
        neighbours.append(image[i-1,j+1])
        neighbours.append(image[i,j+1])
        neighbours.append(image[i+1,j+1])
        neighbours.append(image[i+1,j])
    elif(i>0 and i<dim[0]-1 and j==dim[1]-1):
        neighbours.append(image[i-1,j])
        neighbours.append(image[i+1,j])
        neighbours.append(image[i+1,j-1])
        neighbours.append(image[i,j-1])
        neighbours.append(image[i-1,j-1])
    elif(i==0 and j==0):
        neighbours.append(image[i,j+1])
        neighbours.append(image[i+1,j+1])
        neighbours.append(image[i+1,j])
    elif(i==0 and j==dim[1]-1):
        neighbours.append(image[i+1,j])
        neighbours.append(image[i+1,j-1])
        neighbours.append(image[i,j-1])
    elif(i==dim[0]-1 and j==0):
        neighbours.append(image[i-1,j])
        neighbours.append(image[i,j+1])
        neighbours.append(image[i-1,j+1])
    elif(i==dim[0]-1 and j==dim[1]-1):
        neighbours.append(image[i-1,j])
        neighbours.append(image[i,j-1])
        neighbours.append(image[i-1,j-1])
    return neighbours

def fetchNeighbours1(image,i,j):
    neighbours = [0,0,0,0,0,0,0,0,0,0]
    dim = np.shape(image)
    if(i>0 and i<dim[0]-1 and j>0 and j<dim[1]-1):
        neighbours[2]=image[i-1,j]
        neighbours[3]=image[i-1,j+1]
        neighbours[4]=image[i,j+1]
        neighbours[5]=image[i+1,j+1]
        neighbours[6]=image[i+1,j]
        neighbours[7]=image[i+1,j-1]
        neighbours[8]=image[i,j-1]
        neighbours[9]=image[i-1,j-1]
    elif(i==0 and j>0 and j<dim[1]-1):
        neighbours[4]=image[i,j+1]
        neighbours[5]=image[i+1,j+1]
        neighbours[6]=image[i+1,j]
        neighbours[7]=image[i+1,j-1]
        neighbours[8]=image[i,j-1]
    elif(i==dim[0]-1 and j>0 and j<dim[1]-1):
        neighbours[2]=image[i-1,j]
        neighbours[3]=image[i-1,j+1]
        neighbours[4]=image[i,j+1]
        neighbours[8]=image[i,j-1]
        neighbours[9]=image[i-1,j-1]
    elif(i>0 and i<dim[0]-1 and j==0):
        neighbours[2]=image[i-1,j]
        neighbours[3]=image[i-1,j+1]
        neighbours[4]=image[i,j+1]
        neighbours[5]=image[i+1,j+1]
        neighbours[6]=image[i+1,j]
    elif(i>0 and i<dim[0]-1 and j==dim[1]-1):
        neighbours[2]=image[i-1,j]
        neighbours[6]=image[i+1,j]
        neighbours[7]=image[i+1,j-1]
        neighbours[8]=image[i,j-1]
        neighbours[9]=image[i-1,j-1]
    elif(i==0 and j==0):
        neighbours[4]=image[i,j+1]
        neighbours[5]=image[i+1,j+1]
        neighbours[6]=image[i+1,j]
    elif(i==0 and j==dim[1]-1):
        neighbours[6]=image[i+1,j]
        neighbours[7]=image[i+1,j-1]
        neighbours[8]=image[i,j-1]
    elif(i==dim[0]-1 and j==0):
        neighbours[2]=image[i-1,j]
        neighbours[3]=image[i-1,j+1]
        neighbours[4]=image[i,j+1]
    elif(i==dim[0]-1 and j==dim[1]-1):
        neighbours[8]=image[i-1,j]
        neighbours[9]=image[i,j-1]
        neighbours[2]=image[i-1,j-1]
    return neighbours


def thin1(image,ite):
    image = np.array(image)
    markedPixels= []
    for i in range(1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            neighbours = fetchNeighbours(image,i,j)
            nonZeroNeighboursCount = np.sum(neighbours)/255
            transitionCount = 0
            for k in range(len(neighbours)-1):
                if(neighbours[k]!=neighbours[k+1]):
                    transitionCount+=1
            mark = (image[i,j]>0 and nonZeroNeighboursCount in [2,3,4,5,6] and transitionCount==1)
            #mark = mark and neighbours[5]!=0
            if(ite==1):
                mark = mark and (neighbours[2-2]*neighbours[4-2]*neighbours[6-2])==0 and (neighbours[4-2]*neighbours[6-2]*neighbours[8-2])==0
            else:    
                mark = mark and (neighbours[2-2]*neighbours[4-2]*neighbours[8-2])==0 and (neighbours[2-2]*neighbours[6-2]*neighbours[8-2])==0
            if(mark):
                #image[i,j]=0
                markedPixels.append([i,j])
    for p in markedPixels:
        image[p[0],p[1]]=0
    return image




def hori_thin(image_in,th=7):
    image = np.array(image_in)
    for i in range(image.shape[0]):
        start = -1
        end = -1
        for j in range(image.shape[1]):
            if((image[i,j]!=0)and(start == -1)):
                start = j
            elif((image[i,j] == 0)and(start != -1)):
                end = j-1
                if(((end - start + 1) < th)and((end-start+1)>3)):
                    image[i,start:end+1] = 0
                    s1 = int((start+end)/2)-1
                    e1 = int((start+end)/2)+1
                    image[i,s1:e1+1] = 255
                    #print('start:', start, ' and end: ',end, 'j:', j)
                    #print('s1:',s1,' e1:',e1)
                start = -1
                end = -1
    return image