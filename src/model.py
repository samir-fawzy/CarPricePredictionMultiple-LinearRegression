import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

def ComputeCost(x,y,theta):
    m = len(y)
    predictions = x.dot(theta)
    cost = (1 / (2 * m)) * np.sum((predictions - y) ** 2)
    return cost

def GradienDescent(x,y,iters = 50000,alpha = 0.01):
    m = len(y)
    theta = np.zeros((x.shape[1],1))
    for i in range(iters):
        prediction = x.dot(theta)
        error = prediction - y
        gradient = (1 / m) * x.T.dot(error)
        theta -= alpha * gradient
        print(f"cost at iterations {i} = {ComputeCost(x,y,theta)}")

    np.save("src\\data\\opt_theta.npy",theta)

    with open("src\\data\\linear_model.pkl", "wb") as f:
        pickle.dump(theta, f)   
    return theta

def Predictoin(x,theta):
    predition = x.dot(theta)
    return predition


