import numpy as np
import pandas as pd

class RandomDataGenerator:
    def generate_data(self, n=100, x_var=10, y_var=10, z_var=10, xy_corr=0.0, xz_corr=0.0, yz_corr=0.0):
        """
        Generate random data points with given parameters.

        Parameters:
        - n (int): Number of data points
        - x_var (float): Variability of x
        - y_var (float): Variability of y
        - z_var (float): Variability of z
        - xy_corr (float): Correlation between x and y (-1 to 1)
        - xz_corr (float): Correlation between x and z (-1 to 1)
        - yz_corr (float): Correlation between y and z (-1 to 1)

        Returns:
        - df (DataFrame): Pandas DataFrame containing x, y, and z values
        """
        # Validate correlation inputs
        if not (-1.0 <= xy_corr <= 1.0 and -1.0 <= xz_corr <= 1.0 and -1.0 <= yz_corr <= 1.0):
            raise ValueError("Correlations must be between -1 and 1.")

        # Generate uncorrelated random data
        x = np.random.normal(0, x_var, n)
        y = np.random.normal(0, y_var, n)
        z = np.random.normal(0, z_var, n)

        # Create a covariance matrix based on correlations
        cov_matrix = np.array([
            [x_var**2, xy_corr * x_var * y_var, xz_corr * x_var * z_var],
            [xy_corr * x_var * y_var, y_var**2, yz_corr * y_var * z_var],
            [xz_corr * x_var * z_var, yz_corr * y_var * z_var, z_var**2]
        ])

        # Ensure the covariance matrix is positive semi-definite
        if not np.all(np.linalg.eigvals(cov_matrix) >= 0):
            raise ValueError("Covariance matrix is not positive semi-definite. Adjust correlation values.")

        # Generate correlated data
        mean = [0, 0, 0]
        data = np.random.multivariate_normal(mean, cov_matrix, n)
        x, y, z = data[:, 0], data[:, 1], data[:, 2]

        # Create a pandas DataFrame
        df = pd.DataFrame({"x": x, "y": y, "z": z})

        return df
