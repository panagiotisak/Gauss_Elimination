import numpy as np

def gauss_elimination(A,b):
    A=A.astype(float)#lets A get float arguments
    b=b.astype(float)#lets b get float arguments
    #a function with arguments matrix A nxn and array b nx1
    x = np.zeros(A.shape[0])
    x=x.astype(float)
    #creats an empty array of length n
    dimA = A.shape #get the dimension of A
    dimb = b.shape #get the dimension of b
    if(dimA[1]!=dimA[0] or dimA[1]!=dimb[0] or A[0][0]==0):
        print("matrix A must be nxn and b nx1 so that A*x=b")
        exit()
    else:
        print("A= ",A ,"b= ", b)
    n=dimA[0]
    
    for sub_matrix in range(n-1): 
        #goes through each submatrix when a column is filled with zeroes
        #the last calulation doesnt matter
        for rows in range(sub_matrix+1,n):
            r=A[rows][sub_matrix]/A[sub_matrix][sub_matrix]
            #it must stay the same for the column loop otherwise you get
            # 0 cause A[1][0] is substitued by 0
            b[rows]=b[rows]-b[sub_matrix]*r
            #changing b accordingly
            for columns in range(sub_matrix,n):
                #now we can go through each column 
                #We go through each number in a row and substract 
                #the first row of the sub matrix by a factor r
                #such that the first element is 0
                A[rows][columns]=A[rows][columns]-A[sub_matrix][columns]*r       
    for rows in range(n-1,-1,-1):
        for columns in range(n-1,-1,-1):
            b[rows]=b[rows]-A[rows][columns-1]*x[columns-1]
            
            #x must use the columns so that it matches A
            #I want x to change along with the factor of A, unlike b
        x[rows]=b[rows]/A[rows][rows]
    print("x= ",x)
    

A=np.array([[1,-2,7],
            [-4,5,6],
            [-9,2,-8]])

b=np.array([1,2,5])

gauss_elimination(A,b)

    