import numpy as np
from clean_data import x_testing , y_testing
from model import Predictoin
from data_loader import load_data
import matplotlib.pyplot as plt

theta = np.load("src\\data\\opt_theta.npy")

predictions = Predictoin(x_testing,theta)

df = np.c_[y_testing,predictions]

x_axis = list(range(len(x_testing)))

fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# الرسم الأول
axs[0].plot(x_axis, y_testing, label="Actual Values")
axs[0].plot(x_axis, predictions, label="Prediction Values", c='r')
axs[0].legend()
axs[0].grid(True)
axs[0].set_title("Line Plot")

# الرسم الثاني
axs[1].scatter(x_axis, y_testing, label="Actual Values")
axs[1].scatter(x_axis, predictions, c='r', label="Prediction Values")
axs[1].legend()
axs[1].set_title("Scatter Plot")

plt.savefig("src\\data\\images\\my_plot1")
plt.tight_layout()
plt.show()


