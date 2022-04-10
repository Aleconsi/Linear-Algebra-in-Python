#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Matrix():
    
    def __init__(self, X = [[0]]):
        if isinstance(X, Matrix):
            X = X.X
        assert isinstance(X, list)
        
        self.X = X
        self.lenRow = len(self.X)
        self.lenCol = len(self.X[0]) 
        self.determinant = 0.0
        self.swaps = 0 # Number of swaps to reduce to upper triangular matrix
        self.operationCount = 0
        
    def __str__(self):
        """
        Print the Matrix, each row in new terminal line.

        Returns
        -------
        returnString : str
            String to print.

        """
    
        returnString = ""

        for row in self.X:
            returnString += '\n' + str(row)
        
        return returnString
     
    def __add__(self, other, adding = 1):
        result = Matrix([[self.X[i][j] + adding * other.X[i][j]
                          for j in range(self.lenCol)]
                         for i in range(self.lenRow)])
        if self.lenRow == other.lenRow and self.lenCol == other.lenCol:
            pass
        else:
            print("the matrices have different dimensions, operation is unable to proceed")
         
        return result


    def __sub__(self, other):
        return self.__add__(other, -1)
    

    def __mul__(self, other):
        
        if (not self.areCompatible(other)):
            print("Matrices do not have appropriate dimensions!")
            return
        
        if isinstance(other, (Matrix)):
            result = Matrix([[sum(a*b for a,b in zip(i ,j))
                              for j in zip(*other.X)] for i in self.X])
            return result
        
        elif isinstance(other, (int, float)):            
            result = Matrix([[self.X[i][j] * other for j in range(self.lenCol)]
                             for i in range(self.lenRow)])           
            return result


    def transpose(self):
        result = Matrix([[self.X[j][i] for j in range(self.lenRow)] for i in range(self.lenCol)])
        return result
    
                                   
    def printDimensions(self):
        print(self.lenRow, "x", self.lenCol)
        
        
    def getDimensions(self):
        return self.lenRow, self.lenCol
    
    
    def isColumnVector(self):
        if (len(self.X[0]) == 1):
            return True
        return False
    
    def upperTriangular(self, bVector=None):
        """
        Create an upper triangular matrix.
        
        If bVector is given, creates an upper triangular system.

        Parameters
        ----------
        bVector : Matrix, optional
            Vector b of the linear system. The default is None.

        Returns
        -------
        Matrix
            The upper triangular matrix.
        Tuple(Matrix, Matrix)
            The upper triangular matrix and vector b if parameter bVector is given.
        """
        
        A = self.copyMatrix()
    
        n = A.lenRow
        swaps = 0
        
        if (bVector != None):
            if (bVector.isColumnVector()):
                b = bVector.copyMatrix()   
            else:
                return

        for k in range(0, n - 1):
            if (A.X[k][k] == 0):
                
                A.swapLine(k, k) #recursion
                if (bVector != None):
                    b.swapLine(k, k)

                print("Linear system has no solution!")
                return None, None
                
            for r in range(k + 1, n):
    
                m = A.X[r][k] / A.X[k][k]
                
                for j in range(k, n):
                    A.X[r][j] -= m * A.X[k][j]
                    
                if (bVector != None):
    
                    b.X[r][0] -= m * b.X[k][0]
                
                swaps += 1
        
        self.swaps = swaps  
        
        if (bVector == None):
            return A
        return A, b
    
    def swapLine(self, k, r):
        """
        Swap lines in Matrix until nonzero element
        at row r and column k is found.

        Parameters
        ----------
        k : int
            Index of column (List).
        r : int
            Index of row (List)..

        Returns
        -------
        None.

        """

        if (k == self.lenRow):
            return
    
        if (self.X[r][k] == 0):
            self.swapLine(k, r + 1)
         
        else:
            self.X[k], self.X[r] = self.X[r], self.X[k]
            
        return


    def copyMatrix(self):
        """
        Create a copy of a Matrix.

        Returns
        -------
        Matrix
            A copy of self.
        """
        return Matrix([a[:] for a in self.X])
    

    def rowReduction(self):
        """
        Row reduction of a Matrix.
        
        Operates on a given Matrix.

        Returns
        -------
        Matrix
            Row reduced Matrix.

        """
        
        if not self: return
        next = 0     
        for r in range(self.lenRow):
            if next >= self.lenCol:
                return
            i = r
            while self.X[i][next] == 0:
                i += 1
                if i == self.lenRow:
                    i = r
                    next += 1
                    if self.lenCol == next:
                        return
            self.X[i], self.X[r] == self.X[r],self.X[i]
            h = self.X[r][next]
            self.X[r] = [mrx / float(h) for mrx in self.X[r]]
            for i in range(self.lenRow):
                if i != r:
                    h = self.X[i][next]
                    self.X[i] = [b - h*a for a,b in zip(self.X[r],self.X[i])]
        for i in range(self.lenRow): 
            g = 0
            for idx in self.X[i]:      
                if idx == -0.0:
                    self.X[i][g] = abs(self.X[i][g])
                g +=1  
            next += 1
        return self
    
    def areCompatible(self, other):
        """
        Checks if Matrices have compatible dimensions to be multiplied.

        Parameters
        ----------
        other : Matrix
            Second Matrix.

        Returns
        -------
        bool
            Compatibility of Matrix self and other.

        """
        
        if (isinstance(other, (int, float))):
            return True
        
        r1, c1 = self.getDimensions()
        r2, c2 = other.getDimensions()
        
        if c1 == r2:
            return True
        
        return False
    
    def getDeterminant(self):
        """
        Calculates a determinant of the Matrix.

        Returns
        -------
        float
            The determinant of the Matrix.

        """
        
        det = -1.0
        
        upper = self.upperTriangular()
        
        if (not upper): return
  
        for k in range(0, self.lenRow):

            det *= upper.X[k][k]      
        
        self.determinant = (-1) ** self.swaps * det
        
        return self.determinant
    
    def solveLinear(self, bVector):
        """
        Solves a linear system involving a Matrix and vector b.

        Parameters
        ----------
        bVector : Matrix
            Vector b of the linear system.

        Returns
        -------
        xVector : Matrix
            Vector x as the solution of the linear system.

        """
        
        self.operationCount = 0
        
        upper = self.upperTriangular(bVector)
        AUpper, bUpper = upper
        A = AUpper.X
        b = bUpper.X
        
        xVector = Matrix([[0] for a in range(bVector.lenRow)])
        x = xVector.X
        n = xVector.lenRow 
        
        x[n - 1][0] = b[n - 1][0] / A[n - 1][n - 1] 

        
        for k in range(n - 2, -1, -1):

            res = 0.0
            
            for j in range(k + 1, n):
                
                res += A[k][j] * x[j][0]
                
                self.operationCount += 1
       
            x[k][0] = (1 / A[k][k]) * (b[k][0] - res)
  
        return xVector

    