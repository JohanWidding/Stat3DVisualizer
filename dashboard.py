from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QSlider, QLabel
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from functions.random_data_generator import RandomDataGenerator
from widgets.plot3d import Plot3D
from widgets.show_regression_result import RegressionResults


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        row_layout = QHBoxLayout()  # Create a horizontal layout
        self.regression = RegressionResults()
        self.regression.setFixedWidth(600)

        self.plot = Plot3D()

        row_layout.addWidget(self.regression)
        row_layout.addWidget(self.plot)

        self.layout.addLayout(row_layout)  # Add the horizontal layout to the main layout

        self.sliders_layout = QVBoxLayout()

        # Slider for N
        self.n_slider, self.n_label = self.create_slider("Sample Size (N)", 10, 1000, 100)
        self.sliders_layout.addWidget(self.n_label)
        self.sliders_layout.addWidget(self.n_slider)

        # Sliders for variability
        self.x_var_slider, self.x_var_label = self.create_slider("X Variability", 1, 100, 10)
        self.y_var_slider, self.y_var_label = self.create_slider("Y Variability", 1, 100, 10)
        self.z_var_slider, self.z_var_label = self.create_slider("Z Variability", 1, 100, 10)
        self.sliders_layout.addWidget(self.x_var_label)
        self.sliders_layout.addWidget(self.x_var_slider)
        self.sliders_layout.addWidget(self.y_var_label)
        self.sliders_layout.addWidget(self.y_var_slider)
        self.sliders_layout.addWidget(self.z_var_label)
        self.sliders_layout.addWidget(self.z_var_slider)

        # Sliders for correlation
        self.xy_corr_slider, self.xy_corr_label = self.create_slider("X-Y Correlation", -100, 100, 0)
        self.xz_corr_slider, self.xz_corr_label = self.create_slider("X-Z Correlation", -100, 100, 0)
        self.yz_corr_slider, self.yz_corr_label = self.create_slider("Y-Z Correlation", -100, 100, 0)
        self.sliders_layout.addWidget(self.xy_corr_label)
        self.sliders_layout.addWidget(self.xy_corr_slider)
        self.sliders_layout.addWidget(self.xz_corr_label)
        self.sliders_layout.addWidget(self.xz_corr_slider)
        self.sliders_layout.addWidget(self.yz_corr_label)
        self.sliders_layout.addWidget(self.yz_corr_slider)

        # Add sliders layout to the main layout
        self.layout.addLayout(self.sliders_layout)
        self.setLayout(self.layout)

        # Connect slider signals
        self.n_slider.valueChanged.connect(self.refresh_data)
        self.x_var_slider.valueChanged.connect(self.refresh_data)
        self.y_var_slider.valueChanged.connect(self.refresh_data)
        self.z_var_slider.valueChanged.connect(self.refresh_data)
        self.xy_corr_slider.valueChanged.connect(self.refresh_data)
        self.xz_corr_slider.valueChanged.connect(self.refresh_data)
        self.yz_corr_slider.valueChanged.connect(self.refresh_data)

        self.data_generator = RandomDataGenerator()
        self.refresh_data()

    def create_slider(self, name, min_val, max_val, initial_val):
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(min_val)
        slider.setMaximum(max_val)
        slider.setValue(initial_val)
        label = QLabel(f"{name}: {initial_val}")
        slider.valueChanged.connect(lambda value: label.setText(f"{name}: {value}"))
        return slider, label

    def refresh_data(self):
        n = self.n_slider.value()
        x_var = self.x_var_slider.value()
        y_var = self.y_var_slider.value()
        z_var = self.z_var_slider.value()
        xy_corr = self.xy_corr_slider.value() / 100.0
        xz_corr = self.xz_corr_slider.value() / 100.0
        yz_corr = self.yz_corr_slider.value() / 100.0

        data = self.data_generator.generate_data(n=n, x_var=x_var, y_var=y_var, z_var=z_var,
                                                 xy_corr=xy_corr, xz_corr=xz_corr, yz_corr=yz_corr)

        self.regression.updateResults(data)
        self.plot.updateData(data)