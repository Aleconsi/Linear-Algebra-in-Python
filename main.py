# -*- coding: utf-8 -*-
from matrix import Matrix
# from vector import Vector
import time

def main():

    """ Evidence of correctness of the Linear Systems solution """
    
    filename = "Matrix_file_320.txt"
    
    A = Matrix(readfile(filename))
    b = Matrix([[i for i in range(321)]]).transpose()
    
    start = time.time()
    #Calling the function that solves the linear system Ax = b:
    time.sleep(1)
    
    x = A.solveLinear(b)
    
    end = time.time()
    
    # Let's see if the linear system is solved;
    # As Ax = b, Ax - b must be equal to 0, as shown below. This will prove that the code is indeed correct.
    test = A * x - b
    
    print("\nA:", A, "\n\nx:", x, "\n\nb:", b, "\n\nTest:", test)
    
    # We have to round the values to 0
    print("\nRounded test (should be zeros):\n\n", [round(el[0], 4) for el in test.X])
    
     # this code delivers the time it takes for the algorithm to show the result
    print("\nRuntime of the program is approximately", round((end - start - 1), 4), "seconds")
    
    print("Operation count:", A.operationCount)
    
    
    """ Application """
    
    '''
    unitTimePerTask = Matrix(readfile("price_matrix.txt"))

    costPerUnit = Matrix([[2210912,
                 5023431,
                 5312473,
                 4877940,
                 834603]]).transpose() 
  
    taskPrice = unitTimePerTask.solveLinear(costPerUnit)
    
    print(unitTimePerTask, '\n', costPerUnit, '\n', taskPrice)
    
    testSystem = unitTimePerTask * taskPrice - costPerUnit
    
    print(testSystem)
    
    print("Rounded test (should be zeros):\n\n", [round(el[0], 5) for el in testSystem.X])
    '''

    
def readfile(filepath):
       f = open(filepath,'r')  
       r = f.readline()
       t = r.split()
       r = int(t[2])+1
       
       f.readline()
       
       X=[]
       
       t = f.readline().split()
       for i in range(r):
           rowlist = []
           for j in range(r):
               I,J,A = int(t[0]), int(t[1]), float(t[2])
               if (I == i and J == j):
                   rowlist.append(A)
                   t = f.readline().split()
               else:
                   rowlist.append(0)
           X.append(rowlist)
       return(X)

main()