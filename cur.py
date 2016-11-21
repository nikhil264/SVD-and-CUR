# 100,000 ratings (1-5) from 943 users on 1682 movies. 
# Each user has rated at least 20 movies. 
import numpy as np
import math,sys
from numpy import linalg as LA
from numpy.random import choice
np.set_printoptions(suppress=True)
np.random.seed(5121996)

r = 427
m = 943
n = 1682
totalRatings = 10000
M = np.matrix(np.zeros((m, n)))
r = 0;
if(len(sys.argv) > 1):
	r = int(sys.argv[1])
else:
	r = min(m,n)

# Extracting data from file to matrix M.
f = open("./data.txt", 'r')
for line in f:
	temp = line.split()
	i = int(temp[0])-1
	j = int(temp[1])-1
	rating = int(temp[2])
	M[i,j] = rating
f.close()

# Selecting random columns and rows.
f = LA.norm(M)**2
colProbDist = [(LA.norm(M[:,x])**2)/f for x in xrange(n)]
rowProbDist = [(LA.norm(M[x])**2)/f for x in xrange(m)]
rand_cols = np.random.choice(range(n),r,False,colProbDist)
rand_rows = np.random.choice(range(m),r,False,rowProbDist)

# Initialize C, R, W matrices.
C = np.matrix(np.zeros((m, r)))
R = np.matrix(np.zeros((r, n)))
W = np.matrix(np.zeros((r, r)))
for i in xrange(r):
	C[:,i] = M[:,rand_cols[i]]/math.sqrt(r*colProbDist[rand_cols[i]])
	R[i] = M[rand_rows[i]]/math.sqrt(r*rowProbDist[rand_rows[i]])

for i in xrange(r):
	for j in xrange(r):
		W[i,j] = M[rand_rows[i],rand_cols[j]]

# Calculating U from W using SVD and Moore-Penrose Inverse.
X, Sig, Yt = LA.svd(W, full_matrices=False)
Sig = np.around(Sig, decimals=4)
i = 0
for x in Sig:
	if x != 0:
		Sig[i] = 1/x
	else:
		Sig[i] = 0
	i += 1

Sig = np.matrix(np.diag(Sig))

U = Yt.transpose()*Sig*Sig*X.transpose()
CUR = C*U*R;
print "C :\n" 
print C
print "U :\n"  
print U
print "R :\n"  
print R
print "CUR :\n"  
print CUR
