from PyQt5.QtWidgets import QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from widgets.plot3d import Plot3D
from functions.random_data_generator import RandomDataGenerator
from functions.linear_regression_model import LinearRegressionModel

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.plot = Plot3D()
        self.toolbar = NavigationToolbar(self.plot, self)
        self.data_generator = RandomDataGenerator()
        self.model = LinearRegressionModel()

        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.plot)

        self.setLayout(self.layout)
        self.refresh_data()

    def refresh_data(self):
        x, y, z = self.data_generator.generate_data()
        coefficients, p_value = self.model.fit(x, y, z)
        self.plot.update_plot(x, y, self.model.predict(x, y))
        print(f"Regression Coefficients: {coefficients}, P-value: {p_value}")
