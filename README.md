# SVD-and-CUR

1. SVD
-------------------------
Dataset must consist of space separated (user, movie, rating) tuples.

Edit line 18 to change the filepath to that of the dataset, then run 
"python svd.py" to run the algorithm.
Runs by default with the number of dimensions equal to the rank of the matrix.
To change(reduce) dimensionality, run
"python svd.py <no. of dimensions>"

Outputs U, V transpose, D matrices and Frobenius error.


2. CUR
-------------------------
Dataset must consist of space separated (user, movie, rating) tuples.

Edit line 16 to change the filepath to that of the dataset, then run 
"python cur.py" to run the algorithm.
Runs by default with the number of columns to select equal to the rank of the matrix.
To change(reduce) it, run
"python cur.py <no. of columns/rows>"

Outputs C, U, R, CUR.
