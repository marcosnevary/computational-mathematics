import matplotlib.pyplot as plt
import numpy as np

def plot_neural_network_curve(neural_network, inputs, targets):
    plt.scatter(inputs, targets, color="blue", zorder=3)

    x_values = np.linspace(0, 1)

    y_pred = []
    for x in x_values:
        y_pred.append(neural_network.predict(x))

    plt.title("Neural Network")
    plt.xlabel("Dosages")
    plt.ylabel("Output")
    plt.plot(x_values, y_pred, color="orange")
    plt.grid(True)