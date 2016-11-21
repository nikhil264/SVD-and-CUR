# 100,000 ratings (1-5) from 943 users on 1682 movies. 
# Each user has rated at least 20 movies. 
import sys
import numpy as np
import scipy.sparse.linalg as la
from scipy import linalg
from scipy import sparse
from numpy.linalg import matrix_rank
from numpy import linalg as LA
from numpy.linalg import inv

m = 943
n = 1682
N = 10000
M = np.zeros((m, n))
M = np.matrix(M)
k = 0;
if(len(sys.argv) > 1):
	k = int(sys.argv[1])

# Extracting data from file to matrix M.
f = open("./data.txt", 'r')
for line in f:
	temp = line.split()
	i = int(temp[0])-1
	j = int(temp[1])-1
	rating = int(temp[2])
	M[i,j] = rating

r = matrix_rank(M)
# Outputs right and left-singular vectors, sigma
def svd(M, k=r):
	MT = M.transpose()
	MMT = M*MT
	MTM = MT*M
	if m < n:
		if k < min(m,n):
			s,U = la.eigsh(MMT,k)
		else:
			s,U = LA.eigh(MMT)
		U = np.fliplr(U)
		s = np.flipud(s)
		s = np.sqrt(s)
		S = np.diag(s)
		Vt = np.dot(np.dot(inv(S), U.transpose() ), M)
	else:
		if k < min(m,n):
			s,V = la.eigsh(MTM,k)
		else:
			s,V = LA.eigh(MTM)
		V = np.fliplr(V)
		s = np.flipud(s)
		s = np.sqrt(s)
		S = np.diag(s)
		U = M * V * inv(S)
		Vt = V.transpose
	return np.matrix(U),np.matrix(Vt),np.matrix(S),s

if(len(sys.argv) == 1):
	k = r
if k > r:
	k = r

# Reconstructing original matrix from SVD.
U,V_transpose,S,s = svd(M,k)
M2 = U*S*V_transpose

print "U:"
print U
print "Vt:"
print V_transpose
print "Sigma:"
print S
print "frobineus error"
print LA.norm(abs(M2)-M)
print "No of reduced dimensions:"
print r-k
