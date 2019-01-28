# Matrices (Alpha)
#### Python 3 code to create and operate on matrices
   
### Install using pip:
   
   <code>pip install MatricesM</code>
   
### Import by using:
   <code>import matrices </code>
   #### OR
   <code>from matrices import *</code>
   ##### -<a href=https://github.com/semihM/Matrices/blob/master/matrices.py>matrices.py</a> contains Matrix class and FMatrix, CMatrix and Identity sub-classes
  
   ##### -<a href=https://github.com/semihM/Matrices/blob/master/exampleMatrices.py>exampleMatrices.py</a> contains example matrices
   
   ##### -Check the <a href="https://github.com/semihM/Matrices/projects">project tab</a> to see the progress
-------------- 
Some examples:
--------------
##### Create matrices filled with random integers 
A=Matrix(4) #Creates a 4x4 matrix filled with random integers from the default range which is [-5,5]

B=Matrix([3,5],ranged=[10,25]) #Creates a 3x5 matrix with elements ranged between 10 and 25

----------------------------------------
##### Give list of numbers to create matrices
filled_rows=[[1,2,3],[4,5,6],[7,8,9]]

C=Matrix(listed=filled_rows) #Creates a matrix with the given list of numbers

C1=Matrix(3,"1 0 -1 4 5 5 1 2 2") #Creates a 3x3 matrix from the given string

C2=Matrix([2,4],"5 -2 -3 2 1 0 0 4") #Creates a 2x4 matrix from the given string

----------------------------------------
##### Give a string filled with data and use the numbers in it to create a matrix (Integers only for now)

data="""1,K,60,69900,6325
2,K,30,79000,5200
3,E,52,85500,7825
4,E,57,17100,8375
5,E,55,5500,5450
6,E,68,27200,8550
7,E,41,20500,4500
8,E,20,69000,5050
9,K,33,13200,8325
10,E,37,31800,5975"""

D=Matrix(dim=[10,4],listed=data) #Creates a matrix form of the given string's *integers*, dimension is *required* as [dataAmount,features]

##### OR

##### Read data from files

##### If your file is a table of data AND has a header AND header has numbers in it, use give header parameter 1 or you will get a row of all numbers in the file

##### Currently only works for INTEGER values and if the data in string format doesn't have new lines, it will return a row vector of all values

dataDir="Example\Directory\DATAFILE"

dataMatrix=Matrix(directory=dataDir) #Create a matrix from a table of data

----------------------------------------
##### Create matrices filled with random float numbers

E=FMatrix(6) #Create a matrix filled with random float values in the default range

F=FMatrix(dim=[2,5],randomFill=0) #Fill the matrix with zeros

----------------------------------------
##### Create identity matrices

i=Identity(3) #3x3 identity matrix

i.addDim(2) #Add 2 dimensions to get a 5x5 identity matrix

----------------------------------------
##### Get properties of your matrix

C.grid #Prints the matrix's elements as a grid

C.p #Print the dimension,range,average and the grid

C.directory #Returns the directory of the matrix if there is any given

C.dim #Returns the dimension of the matrix; you can change the dimension, ex: [4,8] can be set to [1,32] where rows carry over as columns in order from left to right

C.string #Returns the string for of the matrix's elements

C.col(n) #Returns nth column of the matrix as a list n∈[1,column amount]

C.row(n) #Returns nth row of the matrix as a list n∈[1,row amount]

C.intForm #Returns integer form of the matrix

C.floatForm #Returns integer form of the matrix

C.ceilForm #Returns a matrix of all the elements' ceiling value

C.floorForm #Returns the same matrix as "intForm"

C.roundForm(decimal=n) #Returns a matrix of elements' rounded up to n decimal digits 

C.uptri #Returns the upper triangular form of the matrix

C.lowtri #Returns the lower triangular form of the matrix

C.avg(n) #Returns the nth column's average, give None as argument to get the all columns' averages

C.inRange(n) #Returns the nth column's range, give None as argument to get the all columns' ranges

C.det #Returns the determinant of the matrix

C.t #Returns the transposed matrix

C.minor(m,n) #Returns the mth row's nth element's minor matrix

C.adj #Returns the adjoint matrix

C.inv #Returns the inversed matrix

C.rank #Returns the rank of the matrix

C.copy #Returns a copy of the matrix

C.summary #Returns the string form of the object 


----------------------------------------

##### Add or remove rows/columns and operate on them

E.add(r=3,lis=[1.0 ,2.5 ,52,242 ,-9883,212, 0.000001, -555,554]) #Make the list given the 3rd row

A.remove(c=2) #Remove the second column 

for a in A.matrix: a[0]%=2 #Change first column's values to the remainder of division by 2 

B @ B.t #Matrix multiplication example

----------------------------------------


##### All calculations below returns True

   A**2 == A * A
   
   A*2==A+A
   
   A.t.t==A
   
   A.adj.t[1][2]==A.minor(2,3).det*-1
   
   (B @ B.inv).roundForm() == Identity(B.dim[0]) # roundForm call is currently required due to %0.001 error rate on calculations 
   
----------------------------------------

#### More examples can be found in <a href=https://github.com/semihM/Matrices/blob/master/exampleMatrices.py>exampleMatrices.py</a>
