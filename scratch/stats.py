from collections import Counter
from statistics  import mean
import math
from functools   import reduce
from scratch.vectors     import sum_of_squares, vector_dot


def mode(x):
    '''returns a  list, might be more than one mode'''
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() 
            if count == max_count]
            
def de_mean(x):
    '''transalate x by substracting its mean so that the results has mean 0'''
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]
    
def variance (x):
    '''assumes x has at least 2 elements'''
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n-1)

def covariance (x, y):
    n = len(x)
    return vector_dot(de_mean(x), de_mean(y)) / (n-1)

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance (x, y) / stdev_x / stdev_y
    else:
        return 0

def standard_deviation(x):
    return math.sqrt(variance(x))

def median(v):
    '''find the middle most value of v'''
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n//2
    if n % 2 == 1:
        #if odd number elements in the list then return middle value
        return sorted_v[midpoint]
    else:
        #if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint 
        return (sorted_v[lo] + sorted_v[hi])/2

def quantile(x, p):
    '''return p-th percentile value in x'''
    p_index = int(p * len(x))
    return sorted(x)[p_index]

def interquartile_range(x):
    return quantile(x, 0.75) - quantile (x, 0.25)

def least_squares_fit(x, y):
    """
    Given two vectors x and y,
    find the least-squares values of alpha and beta
    """
    beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
    alpha = mean(y) - beta * mean(x)
    return alpha, beta

def predict(alpha: float, beta: float, x_i: float) -> float:
    return beta * x_i + alpha

def error(alpha: float, beta: float, x_i: float, y_i: float) -> float:
    """
    The error from predicting beta * x_i + alpha
    when the actual value is y_i
    """
    return predict(alpha, beta, x_i) - y_i

def sum_of_sqerrors(alpha: float, beta: float, x, y) -> float:
    return sum(error(alpha, beta, x_i, y_i) ** 2
               for x_i, y_i in zip(x, y))

def total_sum_of_squares(y) -> float:
    """the total squared variation of y_i's from their mean"""
    return sum(v ** 2 for v in de_mean(y))

def r_squared(alpha: float, beta: float, x, y) -> float:
    """
    the fraction of variation in y captured by the model, which equals
    1 - the fraction of variation in y not captured by the model
    """
    return 1.0 - (sum_of_sqerrors(alpha, beta, x, y) /
                  total_sum_of_squares(y))


