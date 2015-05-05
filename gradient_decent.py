import numpy
import pandas

def compute_cost(features, values, theta):
    """
    Compute the cost of a list of parameters, theta, given a list of features 
    (input data points) and values (output data points).
    """
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    cost_history = []
    #cost_history.append(compute_cost(features, values, theta))
    
    m = len(values)
    for i in range(1,num_iterations):
        h = numpy.dot(features, theta)
        gradient = alpha / m * (values - h)
        theta = theta + numpy.dot(gradient, features) 
        cost_history.append(compute_cost(features, values, theta))

    return theta, pandas.Series(cost_history)
