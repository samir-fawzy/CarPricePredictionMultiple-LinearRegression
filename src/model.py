import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

df = pd.read_csv("src\\data\\CarPriceAfterEditing.csv")

df.insert(0,"base",1)

split_index = int(len(df) * 0.8)


cols = df.shape[1]

x = df.iloc[:split_index,:cols - 2]
y = df.iloc[:split_index,cols - 1]


x_np = x.to_numpy()
y_np = y.to_numpy()

y_np = y_np.reshape(-1,1)

theta = np.zeros((x_np.shape[1],1))

def ComputeCost(x,y,theta):
    m = len(y)
    predictions = x.dot(theta)
    cost = (1 / (2 * m)) * np.sum((predictions - y) ** 2)
    return cost

def GradienDescent(x,y,iters = 10000,alpha = 0.01):
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


