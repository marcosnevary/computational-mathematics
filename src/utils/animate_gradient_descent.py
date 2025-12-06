import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def animate_gradient_descent(self):
    if self.optimize_slope:
        fig, ax = plt.subplots(figsize=(7, 7))
        data_line, = ax.plot([], [], '-', color='orange')
        data_points, = ax.plot([], [], 'o', color='red')

        ax.scatter(self.x_data, self.y_data, color='blue')

        ax.set_xlim(0, 4)
        ax.set_ylim(0, 4)
        ax.grid(True)
        ax.set_xlabel("Weight")
        ax.set_ylabel("Height")
    else:
        intercept_range = np.linspace(0, 2)
        ssr_curve = [
            self._compute_ssr_and_gradients(self.slope, b)[0]
            for b in intercept_range
        ]

        fig, ax = plt.subplots(1, 2, figsize=(14, 7))
        data_line, = ax[0].plot([], [], '-', color='orange')
        data_points, = ax[0].plot([], [], 'o', color='red')

        ax[0].scatter(self.x_data, self.y_data)
        ax[0].set_xlim(0, 4)
        ax[0].set_ylim(0, 4)
        ax[0].grid(True)
        ax[0].set_xlabel("Weight")
        ax[0].set_ylabel("Height")

        point_marker, = ax[1].plot([], [], 'o', color='orange')
        tangent_line, = ax[1].plot([], [], '-', color='orange', zorder=3)

        ax[1].plot(intercept_range, ssr_curve, color='blue')
        ax[1].set_xlabel("Intercept")
        ax[1].set_ylabel("Soma do Erro Quadrático")
        ax[1].set_title("Gradiente Descendente")
        ax[1].grid(True)
    plt.close()

    def update_frame(frame):
        slope = self.slope_history[frame] if self.optimize_slope else self.slope
        intercept = self.intercept_history[frame]
        ssr = self.ssr_history[frame]
        gradient_intercept = self.intercept_gradient_history[frame]
        x_value = self.x_values_history[frame]
        y_value = self.y_values_history[frame]

        x_line = np.linspace(0, 4)
        y_line = slope * x_line + intercept

        data_line.set_data(x_line, y_line)

        if self.stochastic:
            data_points.set_data(x_value, y_value)

        if not self.optimize_slope:
            point_marker.set_data([intercept], [ssr])

            x_tan = np.linspace(0, 2)
            y_tan = ssr + gradient_intercept * (x_tan - intercept)
            tangent_line.set_data(x_tan, y_tan)

            return data_line, data_points, point_marker, tangent_line

        return data_line, data_points

    return FuncAnimation(
        fig,
        update_frame,
        frames=range(len(self.intercept_history)),
        interval=150,
    )