# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:38:28 2018

@author: Semih
"""
from matrices import Matrix,FMatrix,CMatrix,Identity

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

# =============================================================================
# Valid Matrices
# =============================================================================
proj=Matrix(listed=projectGrid)
o=Matrix(dim=8,randomFill=0)
b=Matrix(1)
c=Matrix(dim=[2,4])
d=FMatrix(dim=[4,3])
e=Matrix(8,randomFill=0)
f=FMatrix(dim=6,inRange=[-1250,1250])
g=Matrix(dim=[3,6])
p=Matrix(5,inRange=[0,100])
q=FMatrix(4)

# =============================================================================
# String inputs Matrices
# =============================================================================
validStr1=Matrix(dim=[2,3],listed=" 34-52\n33a c9d88 hello\n--3-")
validStr2=Matrix(listed="312as45\ndid12,,,44\ncc352as45\ndid12,,,44\ncc3-5")
validStr3=Matrix(listed="\n\n\ndd34 5\n\n44\nn659")
validStr4=Matrix(dim=[22,3],listed="""ulke,boy,kilo,yas,cinsiyet
tr,130,30,10,e
tr,125,36,11,e
tr,135,34,10,k
tr,133,30,9,k
tr,129,38,12,e
tr,180,90,30,e
tr,190,80,25,e
tr,175,90,35,e
tr,177,60,22,k
us,185,105,33,e
us,165,55,27,k
us,155,50,44,k
us,160,58,39,k
us,162,59,41,k
us,167,62,55,k
fr,174,70,47,e
fr,193,90,23,e
fr,187,80,27,e
fr,183,88,28,e
fr,159,40,29,k
fr,164,66,32,k
fr,166,56,42,k
""")

# =============================================================================
# InvalidMatrices
# =============================================================================
#You have to give the matrix a valid dimension, or a list to get a dimension, or it won't be a valid matrix
a=Matrix(0)
v=Matrix()
k=Matrix(dim=-1)
l=Matrix(inRange=[0])
m=Matrix(randomFill=1)

# =============================================================================
# Identity Matrices
# =============================================================================
id1=Identity()
id2=Identity(5)
id3=id2.subM(3,3)
id4=Identity(6)

# =============================================================================
"""PRINT THE MATRICES """
# =============================================================================
print('################################') 
print("Matrices created by giving dimensions")
for matrix in [proj,o,b,c,d,e,f,g,p,q,v,a,k,l,m]:
    print(matrix)
print('################################')     
# =============================================================================
"""PRINT THE MATRICES """
# =============================================================================
print('################################') 
print("Matrices created by giving strings or a directory")
for matrix in [validStr1,validStr2,validStr3,validStr4]:
    print(matrix)
print('################################') 
# =============================================================================
"""PRINT THE IDENTITY MATRICES """
# =============================================================================
print('################################') 
print("Identity matrices")
for i in [id1,id2,id3,id4]:
    print(i)
print('################################')     
# =============================================================================
"""PROPERTIES, METHODS CALLS"""   
# =============================================================================
print('################################')  
print("Attribute call outputs\n")
print('################\n')
      
print("d:")
print(d)
print("d.matrix:\n")
print(d.matrix)

print('\n################\n')
      
print("f.subM(1,4,2,3):\n",f.subM(1,4,2,3),"\n")
print(f)
print("f.delDim(4)")
print(f)

print('################')
      
print("g.dim:\n",g.dim)
print("g.inRange:\n",g.inRange)
print("g:",g)      
print("g.remove(3):")
g.remove(3)
print(g)

print('################')
      
h=proj.subM(12,18,5,11)
print("h=proj.subM(12,18,5,11):\n",h)
print("h.avg:",h.avg)
print("\nh.det:",h.det)
print("\nh.rank:",h.rank)
print("\nh.inv:")
print(h.inv)
print("h.minor(3,4):\n",h.minor(3,4),"\n")

print('################')
      
j=g.subM(1,2,1,4)
print("j=g.sub(1,2,1,4):\n",j,"\n")
print("j.summary:\n",j.summary)

print('\n################')
      
print("proj=proj.subM(5,15).copy:\n")
proj=proj.subM(5,15).copy
print(proj)

print('################')
      
print("p:",p)
print("p.det:\n",p.det)
print("\np.adj:\n",p.adj)
print("p.inv:\n")
print(p.inv)

print('################')
      
print("p:")
print(p)
print("p.remove(c=1) and p.remove(r=2)")
p.remove(c=1)
p.remove(r=2)
print(p)
print("p.add(col=2,lis=[55,55,55,55,55]):")
p.add(col=2,lis=[55,55,55,55])
print(p)
print('################\n')
      
r=p.t
print("r:",r)
print("p==r.t:\n")
print(p==r.t)

print("################")
      
print("id2:\n",id2)
print("\nid2.addDim(2):",id2.addDim(2))
print("id2.matrix:\n",id2.matrix)

print('\n################')
      
print("id3:\n")
print(id3)

print('################')
      
print("id4:\n")
print(id4)
print("\nid4.delDim(6):\n")
print(id4.delDim(6))

print('################')
      
print("id4:",id4)
print("\nid4.addDim(10)):\n",id4.addDim(10))

# =============================================================================
"""OPERATIONS ON ELEMENTS"""    
# =============================================================================

print("################################")   
print("Operator examples")
print("################")
      
print("\nc.dim=",c.dim," d.dim:",d.dim)
print("\nmMulti=c@d:")
mMulti=c@d
print(mMulti)
print("\n((((mMulti)+125)**3)%2):")
print(((((mMulti)+125)**3)%2))

print("################\n")
      
print(f)
print("f=f.intForm")
f1=f.intForm
print(f1)
print("f2=f.roundForm(3)")
f2=f.roundForm(2)
print(f2)
print("f2-f1")
f3=f2-f1
print(f3)

print("################")
      
print("r.remove(r=2):")
r.remove(r=2)
print(r)
print("r.rank:",r.rank)
print("\nr[0]=r[1]")
r[0]=r[1]
print(r)
print("r.rank:",r.rank)    

print("################")
      
print("for i in range(len(e.matrix)): e[i][-i-1]=99")
for i in range(len(e.matrix)):e[i][i]=99
print(e)
print("\ne+=50:")
e+=50
print(e)
print("for i in range(len(e.matrixiid)):e[i]=[b%2 for b in e[i]]:\n")
for i in range(len(e.matrix)):e[i]=[b%2 for b in e[i]]
print(e)

print("################")
      
print("\nc%j")
print(c%j)

print("################")
      
print("\na<b")
print(a<b)

# =============================================================================
""" STRING MATRICES' OUTPUTS"""
# =============================================================================
print("\n################################")
print("Strings' matrices:")
print("################\n")
      
for numb,strings in enumerate([validStr1,validStr2,validStr3,validStr4]):
    print("validStr"+str(numb+1)+":")
    print(strings)         
    print('################')
print("")

# =============================================================================
""" Expected Outputs """
# =============================================================================
"""
################################
Matrices created by giving dimensions

Square matrix
Dimension: 20x20
Numbers' range: [0, 99]
Average: 47.3350

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


Square matrix
Dimension: 8x8
Numbers' range: [0, 0]
Average: 0.0000

0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 


Square matrix
Dimension: 1x1
Numbers' range: [-7, -7]
Average: -7.0000

-7 


Dimension: 2x4
Numbers' range: [-10, 10]
Average: -0.2500

  5   5  -5  -8 
  8  10  -7 -10 


Float Matrix
Dimension: 4x3
Numbers' range: [-8.8245, 5.0231]
Average: -1.4222

 5.0231 -3.3691  2.2948 
 3.5688 -3.7884  1.5832 
 3.0131 -7.2040 -4.3368 
-0.8995 -4.1275 -8.8245 


Square matrix
Dimension: 8x8
Numbers' range: [0, 0]
Average: 0.0000

0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 


Float Matrix
Square matrix
Dimension: 6x6
Numbers' range: [-806.5976, 792.4228]
Average: -44.7991

 648.2259  178.0415  -55.0449  175.0604 -222.5840    2.6685 
-555.3000  214.9587 -209.5402   77.1557 -178.4149  -82.3903 
  53.9103  269.8205  117.5727 -231.9779  676.0304 -290.0327 
-362.5199   63.4128   15.8024 -283.3777  241.5628  -96.4011 
-806.5976  -59.4716   -2.8569 -358.0449   43.2339 -139.3578 
-568.0138  633.4714 -355.2145 -784.4355  792.4228 -174.5412 


Dimension: 3x6
Numbers' range: [-10, 10]
Average: -1.8333

  6 -10  -7  -9 -10   0 
  9  -5   4  -7  -7   2 
 -1  10 -10   4   1  -3 


Square matrix
Dimension: 5x5
Numbers' range: [3, 93]
Average: 52.5600

81 91 32 18 43 
18 63  3 32 62 
22 43 12 63 59 
93 36 83 54 26 
89 51 93 66 81 


Float Matrix
Square matrix
Dimension: 4x4
Numbers' range: [-5.7405, 8.3484]
Average: 0.3478

-2.5989 -0.1859  5.7589 -0.0664 
 0.0000  0.9469 -1.0967 -1.5810 
 8.3484 -5.7405  3.3446 -0.9138 
-0.4269  0.5676 -0.6058 -0.1857 

Invalid matrix

Invalid matrix

Invalid matrix

Invalid matrix

Invalid matrix

################################
################################
Matrices created by giving strings or a directory

Dimension: 2x3
Numbers' range: [-52, 88]
Average: 19.1667

 34 -52  33 
  9  88   3 


Dimension: 5x2
Numbers' range: [-5, 352]
Average: 86.4000

312  45 
 12  44 
352  45 
 12  44 
  3  -5 


Dimension: 1x4
Numbers' range: [5, 659]
Average: 185.5000

 34   5  44 659 


Dimension: 22x3
Numbers' range: [9, 193]
Average: 84.7273

130  30  10 
125  36  11 
135  34  10 
133  30   9 
129  38  12 
180  90  30 
190  80  25 
175  90  35 
177  60  22 
185 105  33 
165  55  27 
155  50  44 
160  58  39 
162  59  41 
167  62  55 
174  70  47 
193  90  23 
187  80  27 
183  88  28 
159  40  29 
164  66  32 
166  56  42 

################################
################################
Identity matrices

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


Identity Matrix
Dimension: 3x3

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

################################
################################
Attribute call outputs

################

d:

Float Matrix
Dimension: 4x3
Numbers' range: [-8.8245, 5.0231]
Average: -1.4222

 5.0231 -3.3691  2.2948 
 3.5688 -3.7884  1.5832 
 3.0131 -7.2040 -4.3368 
-0.8995 -4.1275 -8.8245 

d.matrix:

[[5.0231, -3.3691, 2.2948], [3.5688, -3.7884, 1.5832], [3.0131, -7.204, -4.3368], [-0.8995, -4.1275, -8.8245]]

################

f.subM(1,4,2,3):
 
Float Matrix
Dimension: 4x2
Numbers' range: [-209.5402, 269.8205]
Average: 74.3779

 178.0415  -55.0449 
 214.9587 -209.5402 
 269.8205  117.5727 
  63.4128   15.8024 
 


Float Matrix
Square matrix
Dimension: 6x6
Numbers' range: [-806.5976, 792.4228]
Average: -44.7991

 648.2259  178.0415  -55.0449  175.0604 -222.5840    2.6685 
-555.3000  214.9587 -209.5402   77.1557 -178.4149  -82.3903 
  53.9103  269.8205  117.5727 -231.9779  676.0304 -290.0327 
-362.5199   63.4128   15.8024 -283.3777  241.5628  -96.4011 
-806.5976  -59.4716   -2.8569 -358.0449   43.2339 -139.3578 
-568.0138  633.4714 -355.2145 -784.4355  792.4228 -174.5412 

f.delDim(4)

Float Matrix
Square matrix
Dimension: 6x6
Numbers' range: [-806.5976, 792.4228]
Average: -44.7991

 648.2259  178.0415  -55.0449  175.0604 -222.5840    2.6685 
-555.3000  214.9587 -209.5402   77.1557 -178.4149  -82.3903 
  53.9103  269.8205  117.5727 -231.9779  676.0304 -290.0327 
-362.5199   63.4128   15.8024 -283.3777  241.5628  -96.4011 
-806.5976  -59.4716   -2.8569 -358.0449   43.2339 -139.3578 
-568.0138  633.4714 -355.2145 -784.4355  792.4228 -174.5412 

################
g.dim:
 [3, 6]
g.inRange:
 [-10, 10]
g: 
Dimension: 3x6
Numbers' range: [-10, 10]
Average: -1.8333

  6 -10  -7  -9 -10   0 
  9  -5   4  -7  -7   2 
 -1  10 -10   4   1  -3 

g.remove(3):

Dimension: 2x6
Numbers' range: [-10, 9]
Average: -2.8333

  6 -10  -7  -9 -10   0 
  9  -5   4  -7  -7   2 

################
h=proj.subM(12,18,5,11):
 
Square matrix
Dimension: 7x7
Numbers' range: [3, 99]
Average: 51.5306

96 35 31 47 55 58 88 
35 71 89  7  5 44 44 
 5 94 47 69 28 73 92 
97 35 99 16  7 97 57 
57 62 20 72  3 46 33 
38 25 39 11 24 94 72 
72 30 23 88 34 62 99 

h.avg: 51.53061224489796

h.det: 1287494735580

h.rank: 7

h.inv:

Float Matrix
Square matrix
Dimension: 7x7
Numbers' range: [-0.07446221620223706, 0.0709854244777385]
Average: -0.0004

 0.0011  0.0229 -0.0279 -0.0196  0.0155  0.0175  0.0081 
 0.0015  0.0268 -0.0174 -0.0279  0.0197  0.0212 -0.0029 
 0.0048 -0.0282  0.0340  0.0407 -0.0241 -0.0400 -0.0096 
 0.0028 -0.0406  0.0363  0.0380 -0.0121 -0.0393 -0.0074 
 0.0398 -0.0745  0.0710  0.0630 -0.0317 -0.0622 -0.0487 
 0.0017 -0.0272  0.0178  0.0197  0.0007 -0.0011 -0.0167 
-0.0195  0.0605 -0.0501 -0.0545  0.0096  0.0471  0.0410 

h.minor(3,4):
 
Square matrix
Dimension: 6x6
Numbers' range: [3, 99]
Average: 52.1111

96 35 31 55 58 88 
35 71 89  5 44 44 
97 35 99  7 97 57 
57 62 20  3 46 33 
38 25 39 24 94 72 
72 30 23 34 62 99 
 

################
j=g.sub(1,2,1,4):
 
Dimension: 2x4
Numbers' range: [-10, 9]
Average: -2.3750

  6 -10  -7  -9 
  9  -5   4  -7 
 

j.summary:
 Matrix(dim=[2, 4],listed=[[6, -10, -7, -9], [9, -5, 4, -7]],inRange=[-10, 9],randomFill=1)

################
proj=proj.subM(5,15).copy:


Dimension: 5x15
Numbers' range: [0, 99]
Average: 46.9067

 8  2 22 97 38 15  0 40  0 75  4  5  7 78 52 
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 
52 70 95 23  4 60 11 42 69 24 68 56  1 32 56 
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 

################
p: 
Square matrix
Dimension: 5x5
Numbers' range: [3, 93]
Average: 52.5600

81 91 32 18 43 
18 63  3 32 62 
22 43 12 63 59 
93 36 83 54 26 
89 51 93 66 81 

p.det:
 -125306895

p.adj:
 
Square matrix
Dimension: 5x5
Numbers' range: [-13661142, 15660036]
Average: -135298.8000

 -7755489  15660036  -8476146   8666343  -4477389 
  4399339 -12315261   6448316  -7598878   4833269 
  6830993 -13661142   8970592  -8243186   2942173 
  1532552  -1255548  -1743497  -2938439   2360617 
 -3340229   7255401  -3625696   7120883  -4972084 

p.inv:


Float Matrix
Square matrix
Dimension: 5x5
Numbers' range: [-0.12497345816445296, 0.10902147084563862]
Average: 0.0011

 0.0619 -0.1250  0.0676 -0.0692  0.0357 
-0.0351  0.0983 -0.0515  0.0606 -0.0386 
-0.0545  0.1090 -0.0716  0.0658 -0.0235 
-0.0122  0.0100  0.0139  0.0234 -0.0188 
 0.0267 -0.0579  0.0289 -0.0568  0.0397 

################
p:

Square matrix
Dimension: 5x5
Numbers' range: [3, 93]
Average: 52.5600

81 91 32 18 43 
18 63  3 32 62 
22 43 12 63 59 
93 36 83 54 26 
89 51 93 66 81 

p.remove(c=1) and p.remove(r=2)

Square matrix
Dimension: 4x4
Numbers' range: [12, 93]
Average: 53.1875

91 32 18 43 
43 12 63 59 
36 83 54 26 
51 93 66 81 

p.add(col=2,lis=[55,55,55,55,55]):

Dimension: 4x5
Numbers' range: [12, 93]
Average: 53.5500

91 55 32 18 43 
43 55 12 63 59 
36 55 83 54 26 
51 55 93 66 81 

################

r: 
Dimension: 5x4
Numbers' range: [12, 93]
Average: 53.5500

91 43 36 51 
55 55 55 55 
32 12 83 93 
18 63 54 66 
43 59 26 81 

p==r.t:

Same dimension
Same average
All the elements and their positions are same!
True
################
id2:
 
Identity Matrix
Dimension: 5x5

1 0 0 0 0 
0 1 0 0 0 
0 0 1 0 0 
0 0 0 1 0 
0 0 0 0 1 


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
id3:


Identity Matrix
Dimension: 3x3

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

Identity Matrix
Dimension: 0x0


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

################################
Operator examples
################

c.dim= [2, 4]  d.dim: [4, 3]

mMulti=c@d:

Float Matrix
Dimension: 2x3
Numbers' range: [26.866200000000006, 152.793]
Average: 70.5746

 35.0900  33.2525 111.6700 
 63.7761  26.8662 152.7930 


((((mMulti)+125)**3)%2):

Float Matrix
Dimension: 2x3
Numbers' range: [0.21551729319617152, 1.8887290004640818]
Average: 0.9389

1.8887 0.4666 1.0820 
1.6175 0.2155 0.3632 

################


Float Matrix
Square matrix
Dimension: 6x6
Numbers' range: [-806.5976, 792.4228]
Average: -44.7991

 648.2259  178.0415  -55.0449  175.0604 -222.5840    2.6685 
-555.3000  214.9587 -209.5402   77.1557 -178.4149  -82.3903 
  53.9103  269.8205  117.5727 -231.9779  676.0304 -290.0327 
-362.5199   63.4128   15.8024 -283.3777  241.5628  -96.4011 
-806.5976  -59.4716   -2.8569 -358.0449   43.2339 -139.3578 
-568.0138  633.4714 -355.2145 -784.4355  792.4228 -174.5412 

f=f.intForm

Square matrix
Dimension: 6x6
Numbers' range: [-806, 792]
Average: -44.7778

 648  178  -55  175 -222    2 
-555  214 -209   77 -178  -82 
  53  269  117 -231  676 -290 
-362   63   15 -283  241  -96 
-806  -59   -2 -358   43 -139 
-568  633 -355 -784  792 -174 

f2=f.roundForm(3)

Float Matrix
Square matrix
Dimension: 6x6
Numbers' range: [-806.6, 792.42]
Average: -44.7989

 648.2300  178.0400  -55.0400  175.0600 -222.5800    2.6700 
-555.3000  214.9600 -209.5400   77.1600 -178.4100  -82.3900 
  53.9100  269.8200  117.5700 -231.9800  676.0300 -290.0300 
-362.5200   63.4100   15.8000 -283.3800  241.5600  -96.4000 
-806.6000  -59.4700   -2.8600 -358.0400   43.2300 -139.3600 
-568.0100  633.4700 -355.2100 -784.4400  792.4200 -174.5400 

f2-f1

Float Matrix
Square matrix
Dimension: 6x6
Numbers' range: [-0.9799999999999898, 0.960000000000008]
Average: -0.0211

 0.2300  0.0400 -0.0400  0.0600 -0.5800  0.6700 
-0.3000  0.9600 -0.5400  0.1600 -0.4100 -0.3900 
 0.9100  0.8200  0.5700 -0.9800  0.0300 -0.0300 
-0.5200  0.4100  0.8000 -0.3800  0.5600 -0.4000 
-0.6000 -0.4700 -0.8600 -0.0400  0.2300 -0.3600 
-0.0100  0.4700 -0.2100 -0.4400  0.4200 -0.5400 

################
r.remove(r=2):

Square matrix
Dimension: 4x4
Numbers' range: [12, 93]
Average: 53.1875

91 43 36 51 
32 12 83 93 
18 63 54 66 
43 59 26 81 

r.rank: 4

r[0]=r[1]

Square matrix
Dimension: 4x4
Numbers' range: [12, 93]
Average: 53.1250

32 12 83 93 
32 12 83 93 
18 63 54 66 
43 59 26 81 

r.rank: 3
################
for i in range(len(e.matrix)): e[i][-i-1]=99

Square matrix
Dimension: 8x8
Numbers' range: [0, 99]
Average: 12.3750

99  0  0  0  0  0  0  0 
 0 99  0  0  0  0  0  0 
 0  0 99  0  0  0  0  0 
 0  0  0 99  0  0  0  0 
 0  0  0  0 99  0  0  0 
 0  0  0  0  0 99  0  0 
 0  0  0  0  0  0 99  0 
 0  0  0  0  0  0  0 99 


e+=50:

Square matrix
Dimension: 8x8
Numbers' range: [50, 149]
Average: 62.3750

149  50  50  50  50  50  50  50 
 50 149  50  50  50  50  50  50 
 50  50 149  50  50  50  50  50 
 50  50  50 149  50  50  50  50 
 50  50  50  50 149  50  50  50 
 50  50  50  50  50 149  50  50 
 50  50  50  50  50  50 149  50 
 50  50  50  50  50  50  50 149 

for i in range(len(e.matrixiid)):e[i]=[b%2 for b in e[i]]:


Square matrix
Dimension: 8x8
Numbers' range: [0, 1]
Average: 0.1250

1 0 0 0 0 0 0 0 
0 1 0 0 0 0 0 0 
0 0 1 0 0 0 0 0 
0 0 0 1 0 0 0 0 
0 0 0 0 1 0 0 0 
0 0 0 0 0 1 0 0 
0 0 0 0 0 0 1 0 
0 0 0 0 0 0 0 1 

################

c%j

Dimension: 2x4
Numbers' range: [-8, 8]
Average: -0.8750

 5 -5 -5 -8 
 8  0  1 -3 

################

a<b
Lower dimension!
True

################################
Strings' matrices:
################

validStr1:

Dimension: 2x3
Numbers' range: [-52, 88]
Average: 19.1667

 34 -52  33 
  9  88   3 

################
validStr2:

Dimension: 5x2
Numbers' range: [-5, 352]
Average: 86.4000

312  45 
 12  44 
352  45 
 12  44 
  3  -5 

################
validStr3:

Dimension: 1x4
Numbers' range: [5, 659]
Average: 185.5000

 34   5  44 659 

################
validStr4:

Dimension: 22x3
Numbers' range: [9, 193]
Average: 84.7273

130  30  10 
125  36  11 
135  34  10 
133  30   9 
129  38  12 
180  90  30 
190  80  25 
175  90  35 
177  60  22 
185 105  33 
165  55  27 
155  50  44 
160  58  39 
162  59  41 
167  62  55 
174  70  47 
193  90  23 
187  80  27 
183  88  28 
159  40  29 
164  66  32 
166  56  42 

################
"""
# =============================================================================

