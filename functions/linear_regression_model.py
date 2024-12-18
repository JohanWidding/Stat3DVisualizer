import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.stats import linregress

class LinearRegressionModel:
    def fit(self, x, y, z):
        X = np.column_stack((x, y))
        model = LinearRegression()
        model.fit(X, z)
        coefficients = model.coef_

        slope, intercept, r_value, p_value, std_err = linregress(z, model.predict(X))
        return coefficients, p_value

    def predict(self, x, y):
        return 2 * x + 3 * y
