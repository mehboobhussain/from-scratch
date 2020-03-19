import math
from functools import reduce
from typing import List

Vector = List[float]

def vector_add(v, w):
   """adds corresponding elements"""
   return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    """subtracts corresponding elements"""
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    """sums all corresponding elements"""
    result = reduce(vector_add, vectors)
    return result
 
def scalar_multiply(c, v):
    """c is a number, v is a vector"""
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """compute the vector whose ith element is the mean of the ith elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def vector_dot(v, w):    
    ''' multiplies each element of first vector with the second vector 
        and returns the sum 
        parameter
        x: first vector
        y: second vector
        '''
    return sum(vi*wi for vi, wi in zip(v, w))

def sum_of_squares(v):
    return vector_dot(v, v)

def magnitude (v):
    return math.sqrt(sum_of_squares(v))

def squared_distnace(v, w):
    return (sum_of_squares(vector_subtract(v)))

def distance (v, w):
    return magnitude(vector_subtract(v, w))

def shape(A):
  num_rows = len(A)
  num_cols = len(A[0]) if A else 0
  return num_rows, num_cols

def get_rows (A, i):
  return A[i]

def get_cols (A, j):
  return [x[j] for x in A]

def one_diagonal (i,j):
  return 1 if i == j else 0

def make_matrix (rows, cols, fn):
  return [ [fn(i,j) for i in range(cols)] 
          for j in range(rows)]
