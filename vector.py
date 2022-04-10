#!/usr/bin/env python
# coding: utf-8

# In[279]:


# function to read vector.txt
def readfile(filepath):
    f = open(filepath,'r')  
    r = f.readline()
    t = r.split()
    r = int(t[2])
    
    f.readline()
    

    
    t = f.readline().split()
    for i in range(1):
        vec = []
        for j in range(r):
            I,J,A = int(t[0]), int(t[1]), float(t[2])
            if (I == i and J == j):
                vec.append(A)
                t = f.readline().split()
            else:
                rowlist.append(0)
    return vec

### VECTOR CLASS WITHOUT NUMPY
class vector():
    def __init__(self,vector,row,col):
        assert isinstance(row,int)
        assert isinstance(col,int)
        assert isinstance(vector,list)
        self.row=row
        self.col=col
        self.vector=vector
    ### Vector Visualization to check if we are working with vectors or not
    def getVector(self):
        
        if (self.row==1 and self.col>=1) and (len(self.vector)==self.col):
            vec = []
            for i in range(self.row):
                row = []
                for j in range(self.col):

                    row.append(round(self.vector[self.row*i+j],2))
                vec.append(row)
            print("row vector")
            return vec 
                   
        elif (self.row>=1 and self.col==1) and (len(self.vector)==self.row):
            vec =[[] for _ in range(self.row)]
            for j in range(self.row):
                vec[j].append(round(self.vector[j],2))
            print("column vector")
            return vec
        
        else:
            print("this is not a vector or the dimensions dont'match")
        
        
    #### VECTOR SUM
    def __add__(self,other):
        assert isinstance(other,vector)
        if (self.row==1 and self.col>=1) and (other.row==1  and other.col>=1):
            arr=[[] for _ in range(self.row)]
            for i in range(self.row):
                for j in range(self.col):
                    arr[i].append(round(self.vector[j]+other.vector[j],2))
                print("row vector")
                
                return arr
            
        
        
        if (self.row>=1 and self.col==1) and (other.row>=1 and other.col==1):
            arr=[[] for _ in range(self.row)]
            for i in range(self.col):
                for j in range(self.row):
                    arr[j].append(round(self.vector[j]+other.vector[j],2))
                print("column vector")
                return arr
            
        else:
                print("the vectors don't have the same dimension, the sum is not possible !!!")
    ### VECTOR MULTIPLICATION
    def __mul__(self,value):
        if (self.row==1 and self.col>=1):

            arr=[[] for _ in range(self.row)]
            for i in range(self.row):
                for j in range(self.col):
                    arr[i].append(round(self.vector[j]*value,2))
                print("row vector")

                return arr



        elif (self.row>=1 and self.col==1):

            arr=[[] for _ in range(self.row)]
            for i in range(self.col):
                for j in range(self.row):
                    arr[j].append(round(self.vector[j]*value,2))
                print("column vector")
                return arr
        else:
            print("insert a vector and a scalar value")
                    
    ### INNER PRODUCT
    def innerProd(self,other):
        assert isinstance(other,vector)
        if (self.row)==(other.col) and (self.col)==(other.row):
            res=0
            for i in range(len(self.vector)):
                res+=(round(self.vector[i]*other.vector[i],2))
            print("the result of the dot products is a scalar!")
            return res
        else:
            print("remember to transpose the second vector!")
        
    ### CROSS PRODUCT
    def crossProd(self,other):
            assert isinstance(other,vector)
            if (self.row==1 and self.col>=1) and (other.row==1  and other.col>=1) and (len(self.vector)==self.col):
                arr=[[] for _ in range(self.row)]
                for i in range(self.row):
                        arr[i].extend([(self.vector[i+1]*other.vector[i+2])-
                                   (self.vector[i+2]*other.vector[i+1]),-
                                   ((self.vector[i]*other.vector[i+2])-
                                   (self.vector[i+2]*other.vector[i])),+
                                   (self.vector[i]*other.vector[i+1]-
                                   (self.vector[i+1]*other.vector[i]))])
                        print("row vector")
                        return arr
            elif (self.row>=1 and self.col==1) and (other.row>=1 and other.col==1) and (len(self.vector)==self.row):
                arr=[[] for _ in range(self.row)]
                for i in range(self.col):
                    arr[i].append((self.vector[i+1]*other.vector[i+2])-
                                   (self.vector[i+2]*other.vector[i+1]))
                    for j in range(self.col):
                        arr[j+1].append(-((self.vector[i]*other.vector[i+2])-
                                   (self.vector[i+2]*other.vector[i])))
                        for k in range(self.col):
                            arr[k+2].append((self.vector[i]*other.vector[i+1])-
                                   (self.vector[i+1]*other.vector[i]))
                    print("column vector")
                    return arr
            else:
                print("those are not vectors or the dimensions don't match the vector lenght")

                
###TEST
x=readfile("Test_Vector_3.txt")
y=readfile("Test2_Vector_3.txt")
v1=vector(x,1,3)
v2=vector(y,1,3)
v1.crossProd(v2)
v3=vector([833735.6961010001, -14590.992108, -147794.881427],3,1)
v2.innerProd(v3)

