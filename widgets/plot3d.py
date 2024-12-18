import sys
import numpy as np
import pandas as pd
from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.ticker import FuncFormatter
from scipy.stats import t
from sklearn.linear_model import LinearRegression

class Plot3D(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.fig = Figure(constrained_layout=True)
        self.canvas = FigureCanvas(self.fig)

        self.ax = self.fig.add_subplot(111, projection='3d')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.canvas)  # Add only the canvas without the toolbar
        self.setLayout(layout)

    def updateData(self, df, title_name='', has_legend=False, change_formatter=None):
        self.ax.clear()

        # Extract data and column names
        x_data = df.iloc[:, 0].values.reshape(-1, 1)
        y_data = df.iloc[:, 1].values.reshape(-1, 1)
        z_data = df.iloc[:, 2].values
        x_ax_name, y_ax_name, z_ax_name = df.columns[:3]

        # Scatter plot
        self.scatter = self.ax.scatter(x_data, y_data, z_data)

        # Multiple linear regression
        X = np.hstack([x_data, y_data])
        reg = LinearRegression()
        reg.fit(X, z_data)

        # Generate regression plane
        x_range = np.linspace(np.min(x_data), np.max(x_data), 10)
        y_range = np.linspace(np.min(y_data), np.max(y_data), 10)
        x_grid, y_grid = np.meshgrid(x_range, y_range)
        z_grid = reg.intercept_ + reg.coef_[0] * x_grid + reg.coef_[1] * y_grid

        # Plot regression plane
        self.ax.plot_surface(x_grid, y_grid, z_grid, alpha=0.6, cmap='coolwarm')

        # Update labels and grid
        self.ax.grid(True)
        self.ax.set_title(title_name)
        self.ax.set_xlabel(x_ax_name)
        self.ax.set_ylabel(y_ax_name)
        self.ax.set_zlabel(z_ax_name)

        if has_legend:
            self.ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

        if change_formatter:
            self.ax.xaxis.set_major_formatter(FuncFormatter(change_formatter))

        self.canvas.draw()
