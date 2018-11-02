# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:38:28 2018

@author: Semih
"""
from matrices import Matrix,Identity

# =============================================================================
"""Example Inputs"""      
# =============================================================================
projectGrid="""08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""


proj=Matrix(listed=projectGrid)
v=Matrix()
o=Matrix(dim=8,randomFill=0)
a=Matrix(0)
b=Matrix(1)
c=Matrix(listed=" 34-52\n33a c9 ")
d=Matrix(10)
e=Matrix(8,randomFill=0)
f=Matrix(dim=6,inRange=[-1250,1250])
sub=f.sub(1,4,2,3)
g=Matrix(dim=[3,6])
h=proj.sub(12,18,5,11)
j=g.sub(2,3,1,4)
#InvalidMatrices
k=Matrix(dim=-1)
l=Matrix(inRange=[0])
m=Matrix(inRange=[0,0],rangeLock=1)
#Identity Matrices
id1=Identity()
id2=Identity(5)
id3=id2.sub(3,3)
id4=Identity(6)
# =============================================================================
for matrix in [proj,v,o,a,b,c,d,e,f,sub,g,h,j,k,l,m]:
    print(matrix)
    
for i in [id1,id2,id3,id4]:
    print(i)
print('#######################')
print("Attribute call outputs\n")
print("d.matix:\n",d.matrix,"\n")
print('################')
print("f.sub(1,4,2,3):\n",sub,"\n")
print('################')
print("proj.dim:\n",proj.dim,"\n")
print('################')
print("c.inRange:\n",c.inRange,"\n")
print('################')
print("e.matrix:\n",e.summary,"\n")
print('################')
print("f.avg:\n",f.avg,"\n")
print('################')
print("g:\n",g,"\n")
print('################')
print("g.delRC(3):\n")
print(g.delRC(3))
print('################')
print("h=proj.sub(12,18,5,11):\n",h,"\n")
print('################')
print("j=g.sub(2,3,1,4):\n",j,"\n")
print('################')
print("proj.delRC(5,15):\n")
print(proj.delRC(5,15))
print('################')
print("id2.matrix:\n",id2.matrix)
print("\nid2.addDim(2):",id2.addDim(2))
print(id2)
print("id2.matrix:\n",id2.matrix)
print('################')
print("id3.delDim(2) is an invalid expression, because it was obtained by matrix's sub method\n")
print("id3:\n",id3)
print('################')
print("id4:",id4)
print("\nid4.delDim(6):\n")
print(id4.delDim(6))
print('################')
print("id4:",id4)
print("\nid4.addDim(10)):\n",id4.addDim(10)) 
print(id4)
print("")
# =============================================================================
""" Expected Outputs """
# =============================================================================
"""
Square matrix
Dimension: 20x20
Numbers' range: [0, 99]
Average: 47

 8  2 22 97 38 15  0 40  0 75  4  5  7 78 52 12 50 77 91  8 
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48  4 56 62  0 
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30  3 49 13 36 65 
52 70 95 23  4 60 11 42 69 24 68 56  1 32 56 71 37  2 36 91 
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 
24 47 32 60 99  3 45  2 44 75 33 53 78 36 84 20 35 17 12 50 
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 
67 26 20 68  2 62 12 20 95 63 94 39 63  8 40 91 66 49 94 21 
24 55 58  5 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 
21 36 23  9 75  0 76 44 20 45 35 14  0 61 33 97 34 31 33 95 
78 17 53 28 22 75 31 67 15 94  3 80  4 62 16 14  9 53 56 92 
16 39  5 42 96 35 31 47 55 58 88 24  0 17 54 24 36 29 85 57 
86 56  0 48 35 71 89  7  5 44 44 37 44 60 21 58 51 54 17 58 
19 80 81 68  5 94 47 69 28 73 92 13 86 52 17 77  4 89 55 40 
 4 52  8 83 97 35 99 16  7 97 57 32 16 26 26 79 33 27 98 66 
88 36 68 87 57 62 20 72  3 46 33 67 46 55 12 32 63 93 53 69 
 4 42 16 73 38 25 39 11 24 94 72 18  8 46 29 32 40 62 76 36 
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74  4 36 16 
20 73 35 29 78 31 90  1 74 31 49 71 48 86 81 16 23 57  5 54 
 1 70 54 71 83 51 54 69 16 92 33 48 61 43 52  1 89 19 67 48 

Invalid matrix


Square matrix
Dimension: 8x8
Numbers' range: [-122, 125]
Average: -3

  90  -68 -101  116  -88   26    3  -82 
-105  124  -10   80  -49  -25  -54  -51 
-122   16   -2   99   36  125   16  121 
-119  -16 -120  -53 -104   25  118  -22 
 -83  -16   69   29  109  117 -120   23 
-116  -66  -45   75   56  -96 -111  110 
 -43  -89   60   96  -27   -7  124  -69 
  77   25  -64  118  -42   22  -86   -4 


Square matrix
Dimension: 0x0
Numbers' range: [0, 0]
Average: None



Square matrix
Dimension: 1x1
Numbers' range: [48, 48]
Average: 48

48 


Square matrix
Dimension: 2x2
Numbers' range: [-52, 34]
Average: 6

 34 -52 
 33   9 


Square matrix
Dimension: 10x10
Numbers' range: [-121, 119]
Average: -9

  71  -40 -102  -25   57  119   82  -21 -105  -66 
  -1   73 -113  -44   29  -21 -102   45    4 -100 
  17  -57   73   30 -121  -84   86  -43   54    9 
  -4 -110 -119   17   57   61   40   15  -24  -64 
  16   -5   -3    4   70  -73  104  -82  -88    2 
 -12  -51   18   -9   15  -92   41   97    1   29 
 -94  106 -105  -50  -18   -4   65    0  -82  103 
  93  -34    4 -102   15   -6   -8   39  -98  -21 
  73  -57   35   14  -10  119  105  -49  -50 -104 
 -71  -81   45  -75  -28  -58  -60   34  -87   92 


Square matrix
Dimension: 8x8
Numbers' range: [-119, 124]
Average: -2

 108  -47  -59  -27  -49 -117    1  -61 
 -27  -15  -64  123   51   -8   36  -89 
  67   68  -76  -73  -91  -92   18  -40 
  36   51 -108 -119   78  106  -96   17 
   5  112  -61   34  124  -89  -92  111 
 121   98   94   74   -3   84  -24  -40 
 -49   66  -79   -4  101  -47   76 -107 
 -21   70  -60   56  -74 -106   52    5 


Square matrix
Dimension: 6x6
Numbers' range: [-1164, 1171]
Average: 69

 -102   943  -771   117   747  -197 
 1047   788 -1062  -450   906  1171 
 -102   678   507   522     6  -416 
 -454  1010  -290    53 -1004   987 
-1164 -1062  -445   853  -260  -737 
  967    88  -365   508  -604   106 


Dimension: 4x2
Numbers' range: [-1062, 1010]
Average: 225

  943  -771 
  788 -1062 
  678   507 
 1010  -290 


Dimension: 3x6
Numbers' range: [-119, 111]
Average: 3

  94  -87   75   71  -13   44 
-119 -118   32  110  -39  -54 
 111  -85  -19   94   88 -119 


Square matrix
Dimension: 7x7
Numbers' range: [3, 99]
Average: 51

96 35 31 47 55 58 88 
35 71 89  7  5 44 44 
 5 94 47 69 28 73 92 
97 35 99 16  7 97 57 
57 62 20 72  3 46 33 
38 25 39 11 24 94 72 
72 30 23 88 34 62 99 


Dimension: 2x4
Numbers' range: [-119, 111]
Average: 0

-119 -118   32  110 
 111  -85  -19   94 

Invalid matrix

Invalid matrix

Invalid matrix


Identity Matrix
Dimension: 1x1

1 


Identity Matrix
Dimension: 5x5

1 0 0 0 0 
0 1 0 0 0 
0 0 1 0 0 
0 0 0 1 0 
0 0 0 0 1 


Square matrix
Dimension: 3x3
Numbers' range: [0, 1]
Average: 0

1 0 0 
0 1 0 
0 0 1 


Identity Matrix
Dimension: 6x6

1 0 0 0 0 0 
0 1 0 0 0 0 
0 0 1 0 0 0 
0 0 0 1 0 0 
0 0 0 0 1 0 
0 0 0 0 0 1 

#######################
Attribute call outputs

d.matix:
 [[71, -40, -102, -25, 57, 119, 82, -21, -105, -66], [-1, 73, -113, -44, 29, -21, -102, 45, 4, -100], [17, -57, 73, 30, -121, -84, 86, -43, 54, 9], [-4, -110, -119, 17, 57, 61, 40, 15, -24, -64], [16, -5, -3, 4, 70, -73, 104, -82, -88, 2], [-12, -51, 18, -9, 15, -92, 41, 97, 1, 29], [-94, 106, -105, -50, -18, -4, 65, 0, -82, 103], [93, -34, 4, -102, 15, -6, -8, 39, -98, -21], [73, -57, 35, 14, -10, 119, 105, -49, -50, -104], [-71, -81, 45, -75, -28, -58, -60, 34, -87, 92]] 

################
f.sub(1,4,2,3):
 
Dimension: 4x2
Numbers' range: [-1062, 1010]
Average: 225

  943  -771 
  788 -1062 
  678   507 
 1010  -290 
 

################
proj.dim:
 [20, 20] 

################
c.inRange:
 [-52, 34] 

################
e.matrix:
 Summary:

Matrix(
dim=[8, 8],
listed=[[108, -47, -59, -27, -49, -117, 1, -61], [-27, -15, -64, 123, 51, -8, 36, -89], [67, 68, -76, -73, -91, -92, 18, -40], [36, 51, -108, -119, 78, 106, -96, 17], [5, 112, -61, 34, 124, -89, -92, 111], [121, 98, 94, 74, -3, 84, -24, -40], [-49, 66, -79, -4, 101, -47, 76, -107], [-21, 70, -60, 56, -74, -106, 52, 5]],
inRange=[-119, 124],
rangeLock=0,
randomFill=1
) 

################
f.avg:
 69 

################
g:
 
Dimension: 3x6
Numbers' range: [-119, 111]
Average: 3

  94  -87   75   71  -13   44 
-119 -118   32  110  -39  -54 
 111  -85  -19   94   88 -119 
 

################
g.delRC(3):

Current dimension:  [3, 6]
Goal dimension:  [3, 3]
Old grid:
 
  94  -87   75   71  -13   44 
-119 -118   32  110  -39  -54 
 111  -85  -19   94   88 -119 

New grid:

Square matrix
Dimension: 3x3
Numbers' range: [-119, 111]
Average: -13

  94  -87   75 
-119 -118   32 
 111  -85  -19 

################
h=proj.sub(12,18,5,11):
 
Square matrix
Dimension: 7x7
Numbers' range: [3, 99]
Average: 51

96 35 31 47 55 58 88 
35 71 89  7  5 44 44 
 5 94 47 69 28 73 92 
97 35 99 16  7 97 57 
57 62 20 72  3 46 33 
38 25 39 11 24 94 72 
72 30 23 88 34 62 99 
 

################
j=g.sub(2,3,1,4):
 
Dimension: 2x4
Numbers' range: [-119, 111]
Average: 0

-119 -118   32  110 
 111  -85  -19   94 
 

################
proj.delRC(5,15):

Current dimension:  [20, 20]
Goal dimension:  [15, 5]
Old grid:
 
 8  2 22 97 38 15  0 40  0 75  4  5  7 78 52 12 50 77 91  8 
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48  4 56 62  0 
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30  3 49 13 36 65 
52 70 95 23  4 60 11 42 69 24 68 56  1 32 56 71 37  2 36 91 
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 
24 47 32 60 99  3 45  2 44 75 33 53 78 36 84 20 35 17 12 50 
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 
67 26 20 68  2 62 12 20 95 63 94 39 63  8 40 91 66 49 94 21 
24 55 58  5 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 
21 36 23  9 75  0 76 44 20 45 35 14  0 61 33 97 34 31 33 95 
78 17 53 28 22 75 31 67 15 94  3 80  4 62 16 14  9 53 56 92 
16 39  5 42 96 35 31 47 55 58 88 24  0 17 54 24 36 29 85 57 
86 56  0 48 35 71 89  7  5 44 44 37 44 60 21 58 51 54 17 58 
19 80 81 68  5 94 47 69 28 73 92 13 86 52 17 77  4 89 55 40 
 4 52  8 83 97 35 99 16  7 97 57 32 16 26 26 79 33 27 98 66 
88 36 68 87 57 62 20 72  3 46 33 67 46 55 12 32 63 93 53 69 
 4 42 16 73 38 25 39 11 24 94 72 18  8 46 29 32 40 62 76 36 
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74  4 36 16 
20 73 35 29 78 31 90  1 74 31 49 71 48 86 81 16 23 57  5 54 
 1 70 54 71 83 51 54 69 16 92 33 48 61 43 52  1 89 19 67 48 

New grid:

Dimension: 15x5
Numbers' range: [0, 99]
Average: 45

 8  2 22 97 38 
49 49 99 40 17 
81 49 31 73 55 
52 70 95 23  4 
22 31 16 71 51 
24 47 32 60 99 
32 98 81 28 64 
67 26 20 68  2 
24 55 58  5 66 
21 36 23  9 75 
78 17 53 28 22 
16 39  5 42 96 
86 56  0 48 35 
19 80 81 68  5 
 4 52  8 83 97 

################
id2.matrix:
 [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]

id2.addDim(2): 

Identity Matrix
Dimension: 7x7

1 0 0 0 0 0 0 
0 1 0 0 0 0 0 
0 0 1 0 0 0 0 
0 0 0 1 0 0 0 
0 0 0 0 1 0 0 
0 0 0 0 0 1 0 
0 0 0 0 0 0 1 

id2.matrix:
 [[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1]]
################
id3.delDim(2) is an invalid expression, because it was obtained by matrix's sub method

id3:
 
Square matrix
Dimension: 3x3
Numbers' range: [0, 1]
Average: 0

1 0 0 
0 1 0 
0 0 1 

################
id4: 
Identity Matrix
Dimension: 6x6

1 0 0 0 0 0 
0 1 0 0 0 0 
0 0 1 0 0 0 
0 0 0 1 0 0 
0 0 0 0 1 0 
0 0 0 0 0 1 


id4.delDim(6):

All rows have been deleted

################
id4: 
Identity Matrix
Dimension: 0x0



id4.addDim(10)):
 

Identity Matrix
Dimension: 10x10

1 0 0 0 0 0 0 0 0 0 
0 1 0 0 0 0 0 0 0 0 
0 0 1 0 0 0 0 0 0 0 
0 0 0 1 0 0 0 0 0 0 
0 0 0 0 1 0 0 0 0 0 
0 0 0 0 0 1 0 0 0 0 
0 0 0 0 0 0 1 0 0 0 
0 0 0 0 0 0 0 1 0 0 
0 0 0 0 0 0 0 0 1 0 
0 0 0 0 0 0 0 0 0 1 
 """
# =============================================================================

