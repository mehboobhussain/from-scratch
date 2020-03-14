# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from functools import reduce
import math

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

def vector_dot(v, w):    return sum(vi*wi for vi, wi in zip(v, w))

def sum_of_squares(v):
    return vector_dot(v, v)

def magnitude (v):
    return math.sqrt(sum_of_squares(v))

def squared_distnace(v, w):
    return (sum_of_squares(vector_subtract(v)))

def distance (v, w):
    return magnitude(vector_subtract(v, w))

  

score  = [10, 20, 30]
age    = [3, 2, 1]
salary = [1000, 1050, 2000]

print (vector_mean([age, scalar_multiply(5, score)]))
print (vector_mean([score, age, salary]))

print (distance(age, score))
