# 3D Plot Dashboard with Linear Regression

This repository contains a PyQt5-based application that visualizes a 3D plot of a surface derived from a linear regression analysis. The dashboard dynamically updates when the data is tweaked, showing how the statistical significance (p-value) changes based on data variability.

## Features
- **3D Visualization**: A 3D surface plot of the linear regression results.
- **Dynamic Data Generation**: Randomized data with adjustable consistency.
- **Statistical Insights**: Real-time display of regression coefficients and p-value.
- **Interactive Dashboard**: Built using PyQt5 for an interactive user interface.

## File Structure

- **`main.py`**: The entry point of the application. Initializes the main window and dashboard.
- **`3d_plot.py`**: Contains the implementation for the 3D surface plot using Matplotlib.
- **`dashboard.py`**: Manages the integration of the 3D plot and data refresh functionality.
- **`random_data_generator.py`**: Generates random data for visualization, including noise to simulate variability.
- **`stat_model.py`**: Implements a linear regression model, calculates coefficients, and evaluates statistical significance.

## Requirements

To run this project, you'll need:

- Python 3.7+
- PyQt5
- Matplotlib
- NumPy
- Scikit-learn

You can install the required packages using:

```bash
pip install PyQt5 matplotlib numpy scikit-learn
```

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/3d-plot-dashboard.git
   cd 3d-plot-dashboard
   ```

2. Run the application:

   ```bash
   python main.py
   ```

3. Interact with the dashboard to:
   - View the 3D surface plot.
   - Refresh the data to observe changes in the regression analysis and p-value.

## How It Works

1. **Data Generation**: Random data is generated with a linear relationship and added noise.
2. **Linear Regression**: A regression model fits the data to calculate coefficients and evaluate statistical significance.
3. **3D Visualization**: The regression results are visualized as a surface plot.
4. **Real-Time Feedback**: When data is regenerated, the plot and statistical metrics update dynamically.

## Customization
- Adjust the noise level in `random_data_generator.py` to observe different p-values.
- Modify the regression model or visualization parameters to suit your needs.


